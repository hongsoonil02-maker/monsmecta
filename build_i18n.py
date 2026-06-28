import os
import json

locales = {
  "ko": {
    "nav": {"products": "제품소개", "clinical": "임상데이터", "values": "3대 가치", "order": "빠른 발주하기"},
    "hero": {
        "title": "임상 수의사의 해답, MONSMECTA",
        "subtitle": "현장 진료의 까다로운 기준을 통과한 위장관 솔루션. 에스앤제이 동물병원 홍순일 원장이 직접 검증하고 처방합니다.",
        "orderBtn": "원장님 전용 발주서 작성하기",
        "specBtn": "📋 제품 스펙/라벨 보기"
    },
    "values": {
        "title": "몬스멕타의 3대 가치 약속",
        "desc": "수의사 원장님들의 진료 및 경영적 신뢰를 지켜드리는 확실한 기준이 되겠습니다.",
        "online": "온라인 및 펫샵 유통 원천 배제",
        "online_desc": "모든 온라인 쇼핑몰, 오픈마켓, 소셜커머스 및 일반 오프라인 펫샵에 절대 유통하지 않을 것임을 약속드립니다. 오직 동물병원을 통해서만 처방 권위를 유지하실 수 있습니다.",
        "price": "자율 가격 및 마진 구조 보장",
        "price_desc": "합리적 공급가를 보장하며, 실제 판매 가격은 원장님들께서 상황에 맞춰 자율 책정하여 운영하실 수 있습니다. 공급가 대비 압도적 마진율로 병원 경영의 활력이 되어드립니다.",
        "formula": "월등한 학술적 포뮬러",
        "formula_desc": "초미세공정 몬모릴로나이트와 바실러스 서브틸리스 균주를 고함량 배합하여 장 점막 방어막을 빠르게 복구하고, 수액(IV) 치료와 폭발적인 시너지를 일으킵니다."
    },
    "clinical": {
        "title": "수의사가 수의사에게 제안하는 근거",
        "card1_title": "신속한 장 점막 회복 임상",
        "card1_desc": "에스앤제이 동물병원의 실제 처방 케이스를 통해 입증된 유해 물질 차단력과 점막 보호막 형성 속도를 확인하세요.",
        "card2_title": "완벽한 기호성과 투약 편의성",
        "card2_desc": "바쁜 진료 환경과 예민한 환축을 고려하여, 스트레스 없이 자발적인 섭취를 유도하도록 설계되었습니다."
    },
    "order": {
        "title": "동물병원 원장님 전용 퀵 발주서",
        "desc": "입력하신 정보는 병원 인증 및 세금계산서 발행에 엄격하게 사용됩니다.",
        "btn": "선결제 진행하기"
    }
  },
  "en": {
    "nav": {"products": "Products", "clinical": "Clinical Data", "values": "3 Core Values", "order": "Quick Order"},
    "hero": {
        "title": "Clinician's Answer, MONSMECTA",
        "subtitle": "A gut solution that meets the rigorous standards of on-site veterinary care. Verified and prescribed by Dr. James Hong.",
        "orderBtn": "Create Exclusive Order Form",
        "specBtn": "📋 View Specs / Label"
    },
    "values": {
        "title": "MONSMECTA's 3 Core Promises",
        "desc": "We become a reliable benchmark for veterinary directors' clinical and managerial trust.",
        "online": "No Online & Pet-Shop Distribution",
        "online_desc": "We promise never to distribute to online malls, open markets, social commerce, or general offline pet shops. You can maintain prescription authority exclusively through animal hospitals.",
        "price": "Autonomous Pricing & High Margin",
        "price_desc": "We guarantee a reasonable supply price, allowing directors to set the actual retail price autonomously. Overwhelming margin rates provide vitality to hospital management.",
        "formula": "Superior Academic Formula",
        "formula_desc": "High-content blend of ultra-fine Montmorillonite and Bacillus subtilis quickly restores the intestinal mucosal barrier and creates explosive synergy with IV fluid therapy."
    },
    "clinical": {
        "title": "Evidence Proposed by Vets for Vets",
        "card1_title": "Rapid Intestinal Mucosa Recovery",
        "card1_desc": "Verify the blocking power against harmful substances and the speed of mucosal shield formation proven through actual prescription cases at S&J Animal Hospital.",
        "card2_title": "Perfect Palatability & Convenience",
        "card2_desc": "Designed to induce voluntary intake without stress, considering busy clinical environments and sensitive patients."
    },
    "order": {
        "title": "Quick Order Form for Vets",
        "desc": "Entered information is strictly used for hospital verification and tax invoice issuance.",
        "btn": "Proceed with Prepayment"
    }
  },
  "ja": {
    "nav": {"products": "製品紹介", "clinical": "臨床データ", "values": "3大価値", "order": "クイック注文"},
    "hero": {
        "title": "臨床獣医師の答え, MONSMECTA",
        "subtitle": "現場の厳しい基準をクリアした胃腸ソリューション。S&J動物病院のホン院長が直接検証し処方しています。",
        "orderBtn": "院長専用の注文書を作成する",
        "specBtn": "📋 製品スペック/ラベルを見る"
    },
    "values": {
        "title": "モンスメクタの3大価値の約束",
        "desc": "獣医師の皆様の診療および経営的信頼を守る確かな基準となります。",
        "online": "オンラインおよびペットショップ流通の徹底排除",
        "online_desc": "すべてのオンラインモール、オープンマーケット、および一般的なオフラインペットショップには絶対に流通させないことを約束します。動物病院を通じてのみ処方の権威を維持できます。",
        "price": "自律的な価格とマージン構造の保証",
        "price_desc": "合理的な供給価格を保証し、実際の販売価格は院長が状況に合わせて自律的に設定して運営できます。圧倒的なマージン率で病院経営の活力となります。",
        "formula": "優れた学術的フォーミュラ",
        "formula_desc": "超微細工程のモンモリロナイトと枯草菌（Bacillus subtilis）を高濃度で配合し、腸粘膜の防御膜を急速に回復させ、輸液（IV）治療と爆発的なシナジーをもたらします。"
    },
    "clinical": {
        "title": "獣医師が獣医師に提案する根拠",
        "card1_title": "迅速な腸粘膜回復の臨床",
        "card1_desc": "S&J動物病院の実際の処方ケースを通じて実証された有害物質の遮断力と粘膜保護膜形成の速度をご確認ください。",
        "card2_title": "完璧な嗜好性と投薬の利便性",
        "card2_desc": "忙しい診療環境と敏感な患畜を考慮し、ストレスなく自発的な摂取を促すように設計されています。"
    },
    "order": {
        "title": "動物病院長専用クイック注文書",
        "desc": "入力された情報は、病院の認証および税金計算書の発行に厳密に使用されます。",
        "btn": "事前決済を進める"
    }
  },
  "zh": {
    "nav": {"products": "产品介绍", "clinical": "临床数据", "values": "三大价值", "order": "快速订购"},
    "hero": {
        "title": "临床兽医的解答, MONSMECTA",
        "subtitle": "通过现场严苛标准的胃肠道解决方案。由S&J动物医院的洪院长亲自验证并处方。",
        "orderBtn": "创建院长专用订购单",
        "specBtn": "📋 查看产品规格/标签"
    },
    "values": {
        "title": "MONSMECTA 的三大价值承诺",
        "desc": "我们将成为维护兽医临床和经营信任的可靠标准。",
        "online": "彻底排除线上和宠物店销售",
        "online_desc": "我们承诺绝不向任何在线商城、开放市场或普通线下宠物店供货。您只能通过动物医院维持处方权威。",
        "price": "保障自主定价和高利润结构",
        "price_desc": "我们保证合理的供应价格，实际销售价格由院长根据实际情况自主设定。以压倒性的利润率为医院经营注入活力。",
        "formula": "卓越的学术配方",
        "formula_desc": "高含量复配超细蒙脱石和枯草芽孢杆菌，快速修复肠黏膜屏障，并与静脉(IV)输液治疗产生爆发性的协同效应。"
    },
    "clinical": {
        "title": "兽医向兽医提供的临床依据",
        "card1_title": "快速的肠黏膜修复临床",
        "card1_desc": "通过 S&J 动物医院的实际处方案例，验证其阻断有害物质的能力和黏膜保护膜的形成速度。",
        "card2_title": "完美的适口性和投药便利性",
        "card2_desc": "考虑到繁忙的诊疗环境和敏感的患病动物，专为诱导其无压力自发进食而设计。"
    },
    "order": {
        "title": "动物医院院长专用快速订购单",
        "desc": "输入的信息将严格用于医院认证和税务发票开具。",
        "btn": "进行预付款"
    }
  },
  "es": {
    "nav": {"products": "Productos", "clinical": "Datos Clínicos", "values": "3 Valores", "order": "Pedido Rápido"},
    "hero": {
        "title": "La Respuesta Clínica, MONSMECTA",
        "subtitle": "Una solución gastrointestinal que cumple con los rigurosos estándares veterinarios. Verificada y recetada por el Dr. James Hong.",
        "orderBtn": "Crear Formulario de Pedido Exclusivo",
        "specBtn": "📋 Ver Especificaciones"
    },
    "values": {
        "title": "Las 3 Promesas de MONSMECTA",
        "desc": "Nos convertimos en un estándar confiable para la gestión clínica y empresarial de los directores veterinarios.",
        "online": "Exclusión de Ventas en Línea",
        "online_desc": "Prometemos no distribuir nunca a centros comerciales en línea o tiendas de mascotas generales. Mantenemos la autoridad de prescripción exclusivamente a través de clínicas veterinarias.",
        "price": "Precios Autónomos y Margen Garantizado",
        "price_desc": "Garantizamos un precio de suministro razonable, permitiendo a los directores establecer el precio minorista de forma autónoma. Los altos márgenes brindan vitalidad a la gestión.",
        "formula": "Fórmula Académica Superior",
        "formula_desc": "La mezcla de Montmorillonita ultrafina y Bacillus subtilis restaura rápidamente la barrera de la mucosa intestinal, creando una sinergia explosiva con la terapia IV."
    },
    "clinical": {
        "title": "Evidencia Propuesta por Veterinarios",
        "card1_title": "Recuperación Rápida de la Mucosa",
        "card1_desc": "Verifique el poder de bloqueo contra sustancias nocivas y la velocidad de formación del escudo de la mucosa comprobados en casos reales.",
        "card2_title": "Palatabilidad Perfecta",
        "card2_desc": "Diseñado para inducir la ingesta voluntaria sin estrés, considerando entornos clínicos ocupados y pacientes sensibles."
    },
    "order": {
        "title": "Formulario de Pedido para Clínicas",
        "desc": "La información ingresada se usa estrictamente para verificación del hospital y facturación.",
        "btn": "Proceder con el Pago"
    }
  },
  "fr": {
    "nav": {"products": "Produits", "clinical": "Données Cliniques", "values": "3 Valeurs", "order": "Commande Rapide"},
    "hero": {
        "title": "La Réponse Clinique, MONSMECTA",
        "subtitle": "Une solution gastro-intestinale répondant aux normes vétérinaires rigoureuses. Vérifiée et prescrite par le Dr. James Hong.",
        "orderBtn": "Créer un Bon de Commande",
        "specBtn": "📋 Voir les Spécifications"
    },
    "values": {
        "title": "Les 3 Promesses de MONSMECTA",
        "desc": "Nous devenons une référence fiable pour la confiance clinique et managériale des directeurs vétérinaires.",
        "online": "Exclusion des Ventes en Ligne",
        "online_desc": "Nous promettons de ne jamais distribuer via les centres commerciaux en ligne. Vous maintenez l'autorité de prescription exclusivement via les cliniques.",
        "price": "Tarification Autonome et Marge Élevée",
        "price_desc": "Nous garantissons un prix d'approvisionnement raisonnable, permettant aux directeurs de fixer le prix de détail. Un taux de marge exceptionnel dynamise la gestion.",
        "formula": "Formule Académique Supérieure",
        "formula_desc": "Le mélange à haute teneur en Montmorillonite ultra-fine et en Bacillus subtilis restaure rapidement la barrière muqueuse et crée une synergie explosive avec la thérapie IV."
    },
    "clinical": {
        "title": "Preuves Proposées par les Vétérinaires",
        "card1_title": "Récupération Rapide de la Muqueuse",
        "card1_desc": "Vérifiez le pouvoir de blocage contre les substances nocives et la vitesse de formation de la barrière muqueuse prouvés par des cas réels.",
        "card2_title": "Appétence Parfaite",
        "card2_desc": "Conçu pour induire une prise volontaire sans stress, en tenant compte des environnements cliniques occupés et des patients sensibles."
    },
    "order": {
        "title": "Bon de Commande (Cliniques)",
        "desc": "Les informations saisies sont strictement utilisées pour la vérification et la facturation.",
        "btn": "Procéder au Paiement"
    }
  }
}

for lang, data in locales.items():
    os.makedirs(f"src/locales/{lang}", exist_ok=True)
    with open(f"src/locales/{lang}/translation.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
