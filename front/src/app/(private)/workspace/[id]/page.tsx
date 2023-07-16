export default function Workspace({ params }: { params: { id: string } }) {
  return (
    <div>
      <h1>Workspace {params.id}</h1>
    </div>
  );
}
