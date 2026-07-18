def analyze_student_groups():
    """
    Analyzes and demonstrates set operations using two groups of student IDs.
    """
    # Initialize sets of student IDs for better context
    group_a_ids = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    group_b_ids = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    print(f"Group A: {group_a_ids}")
    print(f"Group B: {group_b_ids}\n")

    # 1. Check membership
    target_id = 1
    is_present = target_id in group_a_ids
    print(f"Is Student ID {target_id} present in Group A? : {is_present}")

    # 2. Safely remove an element 
    # (Using discard() is more professional than remove() as it doesn't throw an error if the item is missing)
    group_a_ids.discard(target_id)
    print(f"Group A after removing ID {target_id} : {group_a_ids}\n")

    # --- Set Operations ---
    print("--- Set Operations Results ---")
    
    # 3. Union (|): Combines unique elements from both sets
    all_students = group_a_ids | group_b_ids
    print(f"Union (All unique students) : {all_students}")

    # 4. Intersection (&): Finds common elements in both sets
    common_students = group_a_ids & group_b_ids
    print(f"Intersection (Common students) : {common_students}")

    # 5. Difference (-): Elements in Group A but NOT in Group B
    unique_to_group_a = group_a_ids - group_b_ids
    print(f"Difference (Only in Group A) : {unique_to_group_a}")

    # 6. Symmetric Difference (^): Elements in either group, but not in both
    exclusive_students = group_a_ids ^ group_b_ids
    print(f"Symmetric Difference (Exclusive students) : {exclusive_students}")

    # 7. Check if disjoint: Returns True if sets have no common elements
    are_disjoint = group_a_ids.isdisjoint(group_b_ids)
    print(f"Are the groups completely disjoint? : {are_disjoint}")

if __name__ == "__main__":
    analyze_student_groups()