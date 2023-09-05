import pandas as pd


def extract_works_cited_by_target(all_sociology_works_df, target_oa_ids):
    """
    create a csv of first and second layer references
    """
    # filter all sociology works by openalex ids from the target manuscript
    first_layer = all_sociology_works_df[
        all_sociology_works_df["oa_id"].isin(target_oa_ids)
    ]
    # turn references from string to list
    first_layer["works_referenced_related"] = first_layer[
        "works_referenced_related"
    ].apply(
        lambda x: x.replace("[", "")
        .replace("]", "")
        .replace(",", "")
        .replace("'", "")
        .split(" ")
    )

    # combine first layer references into one list and filter all sociology works again
    combined_refs = [
        item for list in first_layer["works_referenced_related"] for item in list
    ]
    second_layer = all_sociology_works_df[
        all_sociology_works_df["oa_id"].isin(combined_refs)
    ]
    return pd.concat((first_layer, second_layer), axis=0)
