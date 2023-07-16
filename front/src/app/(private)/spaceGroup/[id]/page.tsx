export default function SpaceGroup({ params }: { params: { id: string } }) {
  return (
    <div>
      <h1>SpaceGroup {params.id}</h1>
    </div>
  );
}
