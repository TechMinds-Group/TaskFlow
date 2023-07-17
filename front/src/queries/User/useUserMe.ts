import { useQuery } from "@tanstack/react-query";
import { backConnection } from "../../services/backConnection";

function get() {
  const token = sessionStorage.getItem("accessToken");
  if (token !== null && token !== undefined && token !== "") {
    return backConnection.get("/auth/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  }
}

export const useUserMe = () => {
  const { data, isLoading, refetch } = useQuery(["userAuth"], get);

  return {
    data,
    isLoading,
  };
};
