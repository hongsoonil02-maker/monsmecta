import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Load translation resources
const resources = {
    ko: {
        translation: require('./locales/ko/translation.json'),
    },
    en: {
        translation: require('./locales/en/translation.json'),
    },
    ja: {
        translation: require('./locales/ja/translation.json'),
    },
    zh: {
        translation: require('./locales/zh/translation.json'),
    },
    es: {
        translation: require('./locales/es/translation.json'),
    },
    fr: {
        translation: require('./locales/fr/translation.json'),
    },
};

i18n.use(initReactI18next).init({
    resources,
    lng: 'ko', // default language
    fallbackLng: 'en',
    interpolation: {
        escapeValue: false, // React already escapes
    },
});

export default i18n;
