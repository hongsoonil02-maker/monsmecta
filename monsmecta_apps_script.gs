/**
 * Monsmecta 랜딩페이지 주문/샘플 신청 Google Apps Script
 * - Google Sheets에 적재하는 기존 doPost()를 이 파일로 교체하세요.
 * - 중복 차단: ① requestId 멱등성 ② 전화번호(또는 사업자번호) 최근 30일 중복
 * - 응답: { status: 'ok' } / { status: 'duplicate', reason } / { status: 'error' }
 */
var SHEET_NAME = ''; // 비워두면 첫 번째 시트 사용. 예: '응답'
var DUP_DAYS = 30;   // 동일 전화번호/사업자번호 재신청 차단 기간(일)
var PHONE_FIELD = 'phone';      // 샘플 폼 전화번호 컬럼명
var ORDER_FIELD = 'bizNumber';  // 발주 폼 사업자번호 컬럼명

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(15000);
  try {
    var body = parseBody(e);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = SHEET_NAME ? ss.getSheetByName(SHEET_NAME) : ss.getSheets()[0];
    if (!sheet) return respond({ status: 'error', message: 'sheet not found' });

    var now = new Date();
    var data = sheet.getDataRange().getValues();
    var headers = data[0] || [];
    var idx = function (name) { return headers.indexOf(name); };

    // ① requestId 멱등성: 같은 요청 ID가 이미 있으면 그대로 성공 응답(중복 적재 안 함)
    var rid = String(body.requestId || '').trim();
    var ridIdx = idx('requestId');
    if (rid && ridIdx > -1) {
      for (var r = 1; r < data.length; r++) {
        if (String(data[r][ridIdx] || '').trim() === rid) {
          return respond({ status: 'duplicate', reason: 'requestId' });
        }
      }
    }

    // ② 최근 중복: 같은 전화번호(샘플) 또는 사업자번호(발주)가 DUP_DAYS 이내면 차단
    var keyVal = String(body[PHONE_FIELD] || body[ORDER_FIELD] || '').replace(/[^0-9]/g, '');
    var keyIdx = idx(PHONE_FIELD) > -1 ? idx(PHONE_FIELD) : (idx(ORDER_FIELD) > -1 ? idx(ORDER_FIELD) : -1);
    var tsIdx = idx('timestamp');
    if (keyVal && keyIdx > -1) {
      for (var r2 = 1; r2 < data.length; r2++) {
        var existing = String(data[r2][keyIdx] || '').replace(/[^0-9]/g, '');
        if (existing && existing === keyVal) {
          var recent = true;
          if (tsIdx > -1) {
            var dt = new Date(data[r2][tsIdx]);
            recent = isNaN(dt.getTime()) || (now - dt) < DUP_DAYS * 86400000;
          }
          if (recent) return respond({ status: 'duplicate', reason: 'recent' });
        }
      }
    }

    // ③ 헤더에 없는 새 필드 자동 추가
    var extraFields = [];
    for (var k in body) {
      if (headers.indexOf(k) === -1) extraFields.push(k);
    }
    for (var i = 0; i < extraFields.length; i++) {
      sheet.getRange(1, headers.length + i + 1).setValue(extraFields[i]);
    }

    // ④ 행 적재
    var row = [];
    for (var h = 0; h < headers.length; h++) row.push(body[headers[h]] !== undefined ? body[headers[h]] : '');
    for (var j = 0; j < extraFields.length; j++) row.push(body[extraFields[j]] || '');
    sheet.appendRow(row);

    return respond({ status: 'ok', requestId: rid });
  } catch (err) {
    return respond({ status: 'error', message: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/** urlencoded / multipart / JSON 본문을 모두 파싱 */
function parseBody(e) {
  var out = {};
  if (e.parameter) for (var k in e.parameter) out[k] = e.parameter[k];
  var pd = e.postData;
  if (!pd || !pd.contents) return out;
  var type = String(pd.type || '').toLowerCase();
  var body = pd.contents;

  if (type.indexOf('application/x-www-form-urlencoded') > -1) {
    var pairs = body.split('&');
    for (var i = 0; i < pairs.length; i++) {
      var kv = pairs[i].split('=');
      if (kv[0]) out[decodeURIComponent(kv[0])] = decodeURIComponent((kv[1] || '').replace(/\+/g, ' '));
    }
  } else if (type.indexOf('multipart/form-data') > -1) {
    var m = type.match(/boundary=(?:"([^"]+)"|([^;]+))/i);
    var boundary = m ? (m[1] || m[2] || '').trim() : '';
    if (boundary) {
      var parts = body.split('--' + boundary);
      for (var p = 0; p < parts.length; p++) {
        var pm = parts[p].match(/name="([^"]+)"[\s\S]*?\r\n\r\n([\s\S]*)$/);
        if (pm) out[pm[1]] = pm[2].replace(/\r\n$/, '');
      }
    }
  } else {
    try { var j = JSON.parse(body); for (var k2 in j) out[k2] = j[k2]; } catch (err) { /* ignore */ }
  }
  return out;
}

function respond(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
