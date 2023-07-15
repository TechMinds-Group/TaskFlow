import styles from "./page.module.css";

export default function Home() {
  const environment = process.env.NEXT_PUBLIC_BASE_URL;
  return (
    <main className={styles.main}>
      <p>{environment}</p>
    </main>
  );
}
