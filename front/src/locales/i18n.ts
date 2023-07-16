import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import { en } from "./translations/en";
import { de } from "./translations/de";
import { es } from "./translations/es";
import { ptbr } from "./translations/ptbr";
import { zh } from "./translations/zh";
import { ru } from "./translations/ru";
import { ja } from "./translations/ja";

i18n.use(initReactI18next).init({
  resources: {
    ptbr: { translation: ptbr },
    en: { translation: en },
    de: { translation: de },
    es: { translation: es },
    ja: { translation: ja },
    ru: { translation: ru },
    zh: { translation: zh },
  },
  lng: "ptbr",
  fallbackLng: "ptbr",
  interpolation: {
    escapeValue: false,
  },
});
