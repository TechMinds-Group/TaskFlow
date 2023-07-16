import { usePathname } from "next/navigation";
import nProgress from "nprogress";
import { useEffect, useState } from "react";
import "../styles/nProgress.css";

export function useNProgress() {
  const location = usePathname();
  const [visible, setVisible] = useState(false);

  nProgress.configure({
    showSpinner: false,
  });

  useEffect(() => {
    if (!visible) {
      nProgress.start();
      setVisible(true);
    }

    if (visible) {
      nProgress.done();
      setVisible(false);
    }

    if (!visible) {
      setVisible(false);
      nProgress.done();
    }

    return () => {
      nProgress.done();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [location]);
  return visible;
}
