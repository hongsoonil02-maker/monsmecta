import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

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

const syncDocumentLanguage = (language) => {
    if (typeof document === 'undefined') return;
    document.documentElement.lang = language;
};

i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
        resources,
        fallbackLng: 'ko',
        supportedLngs: ['ko', 'en', 'ja', 'zh', 'es', 'fr', 'de', 'th', 'vi', 'ru', 'pt', 'ar', 'id', 'ms', 'tr'],
        interpolation: { escapeValue: false },
        returnNull: false,
        detection: {
            order: ['querystring', 'cookie', 'localStorage', 'sessionStorage', 'navigator', 'htmlTag', 'path', 'subdomain'],
            caches: ['localStorage', 'cookie'],
        }
    });

syncDocumentLanguage(i18n.language);
i18n.on('languageChanged', syncDocumentLanguage);

export default i18n;

