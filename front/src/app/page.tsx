"use client";
import { t } from "i18next";
import { useRouter } from "next/navigation";
import { QueryClientProvider } from "react-query";
import { queryClient } from "../services/queryClient";
import "../locales/i18n";

export default function Home() {
  const router = useRouter();

  return (
    <QueryClientProvider client={queryClient}>
      <main>
        <button onClick={() => router.push("login")}>
          {t("nav.register")}
        </button>
      </main>
    </QueryClientProvider>
  );
}
