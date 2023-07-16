export default function Project({ params }: { params: { id: string } }) {
  return (
    <div>
      <h1>Project {params.id}</h1>
    </div>
  );
}
