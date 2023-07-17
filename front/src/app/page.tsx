"use client";
import { t } from "i18next";
import { useRouter } from "next/navigation";
import "../locales/i18n";

export default function Home() {
  const router = useRouter();

  return (
    <main>
      <button onClick={() => router.push("login")}>{t("nav.register")}</button>
    </main>
  );
}
