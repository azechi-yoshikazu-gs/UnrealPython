import unreal

new_material_name = "M_NewMaterial"
material_folder_path = "/Game/Materials"

new_material_path = material_folder_path + "/" + new_material_name

new_material = unreal.Material()

if unreal.EditorAssetLibrary.does_asset_exist(new_material_path):
    print(new_material_path + " does exist.")
    new_material = unreal.EditorAssetLibrary.load_asset(new_material_path)
else:
    print(new_material_path + " does not exist.")
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    factory = unreal.MaterialFactoryNew()
    new_material = asset_tools.create_asset("M_NewMaterial", "/Game/Materials", unreal.Material, factory)

unreal.EditorAssetLibrary.save_loaded_asset(new_material)

# new_material = asset_tools.create_asset_with_dialog("M_NewMaterial", "/Game/Materials", unreal.Material, factory)