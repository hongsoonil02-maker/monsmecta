import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import translationKo from './locales/ko/translation.json';
import translationEn from './locales/en/translation.json';
import translationJa from './locales/ja/translation.json';
import translationZh from './locales/zh/translation.json';
import translationEs from './locales/es/translation.json';
import translationFr from './locales/fr/translation.json';
import translationDe from './locales/de/translation.json';
import translationTh from './locales/th/translation.json';
import translationVi from './locales/vi/translation.json';
import translationRu from './locales/ru/translation.json';
import translationPt from './locales/pt/translation.json';
import translationAr from './locales/ar/translation.json';
import translationId from './locales/id/translation.json';
import translationMs from './locales/ms/translation.json';
import translationTr from './locales/tr/translation.json';

// Load translation resources
const resources = {
    ko: { translation: translationKo },
    en: { translation: translationEn },
    ja: { translation: translationJa },
    zh: { translation: translationZh },
    es: { translation: translationEs },
    fr: { translation: translationFr },
    de: { translation: translationDe },
    th: { translation: translationTh },
    vi: { translation: translationVi },
    ru: { translation: translationRu },
    pt: { translation: translationPt },
    ar: { translation: translationAr },
    id: { translation: translationId },
    ms: { translation: translationMs },
    tr: { translation: translationTr },
};

const getBrowserLanguage = () => {
    if (typeof navigator === 'undefined') return 'ko';
    const browserLng = navigator.language || navigator.userLanguage;
    if (!browserLng) return 'ko';
    const langCode = browserLng.split('-')[0].toLowerCase();
    const supported = ['ko', 'en', 'ja', 'zh', 'es', 'fr', 'de', 'th', 'vi', 'ru', 'pt', 'ar', 'id', 'ms', 'tr'];
    return supported.includes(langCode) ? langCode : 'en';
};

const syncDocumentLanguage = (language) => {
    if (typeof document === 'undefined') return;
    document.documentElement.lang = language;
};

i18n.use(initReactI18next).init({
    resources,
    lng: getBrowserLanguage(), // automatically detected language
    fallbackLng: 'en',
    interpolation: {
        escapeValue: false, // React already escapes
    },
});

syncDocumentLanguage(i18n.language || getBrowserLanguage());

i18n.on('languageChanged', syncDocumentLanguage);

export default i18n;
