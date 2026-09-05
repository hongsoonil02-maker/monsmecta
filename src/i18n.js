import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

// 번역 리소스는 언어별로 동적 import 하여 초기 번들에서 제외한다.
// Vite가 각 JSON을 개별 청크로 분리하고, 필요한 시점에만 네트워크로 가져온다.
const localeLoaders = {
    ko: () => import('./locales/ko/translation.json'),
    en: () => import('./locales/en/translation.json'),
    ja: () => import('./locales/ja/translation.json'),
    zh: () => import('./locales/zh/translation.json'),
    es: () => import('./locales/es/translation.json'),
    fr: () => import('./locales/fr/translation.json'),
    de: () => import('./locales/de/translation.json'),
    th: () => import('./locales/th/translation.json'),
    vi: () => import('./locales/vi/translation.json'),
    ru: () => import('./locales/ru/translation.json'),
    pt: () => import('./locales/pt/translation.json'),
    ar: () => import('./locales/ar/translation.json'),
    id: () => import('./locales/id/translation.json'),
    ms: () => import('./locales/ms/translation.json'),
    tr: () => import('./locales/tr/translation.json'),
};

const SUPPORTED_LANGS = Object.keys(localeLoaders);

const loadedLangs = new Set();

const loadLanguage = async (lang) => {
    if (!localeLoaders[lang] || loadedLangs.has(lang)) return;
    try {
        const mod = await localeLoaders[lang]();
        i18n.addResourceBundle(lang, 'translation', mod.default || mod, true, true);
        loadedLangs.add(lang);
    } catch {
        // 로드 실패 시 fallbackLng(ko)로 표시된다.
    }
};

const getInitialLanguage = () => {
    if (typeof window === 'undefined') return 'ko';
    try {
        const urlParams = new URLSearchParams(window.location.search);
        const langParam = urlParams.get('lang') || urlParams.get('lng');
        if (langParam && SUPPORTED_LANGS.includes(langParam)) {
            localStorage.setItem('monsmecta_user_lang', langParam);
            return langParam;
        }
        const userSaved = localStorage.getItem('monsmecta_user_lang');
        if (userSaved && SUPPORTED_LANGS.includes(userSaved)) {
            return userSaved;
        }

        // 브라우저 언어 자동 감지 (navigator.languages 우선, 그 다음 navigator.language)
        const browserLangs = navigator.languages ? [...navigator.languages] : [navigator.language || 'ko'];
        for (const raw of browserLangs) {
            if (!raw) continue;
            const code = raw.toLowerCase().split('-')[0];
            if (SUPPORTED_LANGS.includes(code)) {
                localStorage.setItem('monsmecta_user_lang', code);
                return code;
            }
        }
    } catch {
        // ignore
    }
    return 'ko';
};

const syncDocumentLanguage = (language) => {
    if (typeof document === 'undefined') return;
    document.documentElement.lang = language || 'ko';
    // RTL support for Arabic
    document.documentElement.dir = language === 'ar' ? 'rtl' : 'ltr';
};

const initialLang = getInitialLanguage();

// 언어 변경 시 아직 로드되지 않은 번역을 온디맨드로 가져온다.
i18n.on('languageChanged', (lng) => {
    syncDocumentLanguage(lng);
    try {
        localStorage.setItem('monsmecta_user_lang', lng);
    } catch { /* ignore */ }
    if (!loadedLangs.has(lng) && localeLoaders[lng]) {
        loadLanguage(lng).then(() => {
            // 로드 도중 사용자가 다른 언어로 다시 전환했을 수 있으므로,
            // 현재 선택이 여전히 이 언어일 때만 리렌더를 유도한다.
            if (i18n.language === lng) {
                i18n.changeLanguage(lng);
            }
        });
    }
});

// 초기 언어와 fallback(ko) 번들을 로드한 뒤 i18next를 초기화한다.
// main.jsx 에서 이 Promise를 await 하여 초기 렌더 시 번역이 준비되도록 한다.
export const i18nReady = (async () => {
    // 초기 언어 + fallback(ko)의 번들 데이터를 먼저 확보한다.
    const initialResources = {};
    const langsToPreload = initialLang === 'ko' ? ['ko'] : ['ko', initialLang];
    await Promise.all(
        langsToPreload.map(async (lang) => {
            try {
                const mod = await localeLoaders[lang]();
                initialResources[lang] = { translation: mod.default || mod };
                loadedLangs.add(lang);
            } catch {
                // ignore
            }
        })
    );

    await i18n
        .use(LanguageDetector)
        .use(initReactI18next)
        .init({
            resources: initialResources,
            lng: initialLang,
            fallbackLng: 'ko',
            supportedLngs: SUPPORTED_LANGS,
            interpolation: { escapeValue: false },
            returnNull: false,
            detection: {
                order: ['querystring', 'localStorage'],
                lookupQuerystring: 'lang',
                lookupLocalStorage: 'monsmecta_user_lang',
                caches: ['localStorage'],
            },
        });

    syncDocumentLanguage(i18n.language || initialLang);
    return i18n;
})();

export default i18n;
