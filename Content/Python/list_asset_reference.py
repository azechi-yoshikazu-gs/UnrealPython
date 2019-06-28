import unreal

# Collect all assets
all_asset_string = unreal.EditorAssetLibrary.list_assets("/Game/", True, False)
num_target_assets = len(all_asset_string)

referenced_assets = []
non_referenced_assets = []

with unreal.ScopedSlowTask(num_target_assets) as slow_find_task:
    slow_find_task.make_dialog(True)
    for asset_string in all_asset_string:
        asset_data = unreal.EditorAssetLibrary.find_asset_data(asset_string)        
        if (not asset_data.is_valid() or asset_data.is_redirector()):
            slow_find_task.enter_progress_frame(1, asset_string)
            continue
        if(True):
            # Find referencers
            referencers = unreal.EditorAssetLibrary.find_package_referencers_for_asset(asset_string, False)
            
            if(len(referencers) == 0):
                referenced_assets.append(asset_string)
            else:
                non_referenced_assets.append(asset_string)
        # if pressed "Cancel" button on dialog, task is cancel.
        if slow_find_task.should_cancel():
            print("Task cancelled.")
            del referenced_assets[:]
            del non_referenced_assets[:]
            break
        
        # Advance progress
        slow_find_task.enter_progress_frame(1, asset_string)
        
# Display
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("[Find assets] " + str(num_target_assets))
print("[referenced assets] " + str(len(referenced_assets)))
for asset_string in referenced_assets:
    print("    " + asset_string)
print("---------------------")
print("[Non referenced assets] " + str(len(non_referenced_assets)))
for asset_string in non_referenced_assets:
    print("    " + asset_string)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
