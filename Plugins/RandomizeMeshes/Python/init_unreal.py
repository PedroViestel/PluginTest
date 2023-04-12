import unreal
import csv
import os
import package_solver

package_solver.PackageSolver.install_missing_packages()

@unreal.uclass()
class PythonExposedClass(unreal.BlueprintFunctionLibrary):
    def __init__(self):
        super().__init__()

    @unreal.ufunction(static=True, params=[unreal.Array(unreal.RandomizedMesh)], ret=bool)
    def add_random_mesh_to_data_table(meshes: unreal.Array(unreal.RandomizedMesh)):
        try:
            file_path = unreal.Paths.project_intermediate_dir() + "meshes_to_data_table.csv"
            unreal.log_warning(file_path)

            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                for x in meshes:
                    mesh: unreal.RandomizedMesh = x
                    writer.writerow([mesh.name, mesh.position, mesh.rotation, mesh.type])

            return True
        except:
            return False
