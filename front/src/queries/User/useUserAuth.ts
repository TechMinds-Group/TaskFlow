import { useMutation } from "@tanstack/react-query";
import { useRouter } from "next/router";
import { backConnection } from "../../services/backConnection";
import { useAlertError } from "../../store/useAlertError";
import { useAuth } from "../../store/useAuth";

type User = {
  name: string;
  password: string;
};

type Data = {
  data: {
    token: string;
  };
};

function post({ name, password }: User) {
  if (name && password) {
    return backConnection.post("/auth/login", {
      name,
      password,
    });
  }
}

export const useUserAuth = () => {
  const router = useRouter();
  const { handleError } = useAlertError();
  const { Login } = useAuth();
  const { mutate } = useMutation(
    (newTodo: User) => {
      return post(newTodo);
    },
    {
      onSuccess: (data: Data) => {
        Login(data.data.token);
        router.push("/home");
        handleError({
          message: "Login realizado com sucesso!",
          status: "success",
        });
      },
      onError: (error: any) => {
        handleError({
          message: "Dados inválidos!",
          status: "error",
        });
      },
    }
  );

  return {
    mutate,
  };
};
