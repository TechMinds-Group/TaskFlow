"use client";

import { Errors } from "../components/Errors";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <Errors.Root>
        <Errors.BadRequest />
      </Errors.Root>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
