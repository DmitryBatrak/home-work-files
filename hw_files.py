def read_cook_book_from_file(*, file_name: str) -> dict:
    """
    The function reads the file and converts its dictionary
    :param file_name: The name of the file with the data about the ingredients. The file is in this folder!
    :return: Dictionary of the Book of Recipes
    """
    with open(file_name, "r", encoding="utf-8") as f:
        file_list = []
        cook_book = dict()
        for line in f:
            file_list.append(line.strip())

        for ind, element in enumerate(file_list):
            try:
                ingredient_value = int(element)
                all_ingredients = []
                counter = 1
                while ingredient_value != 0:
                    ingredients = dict()
                    ingredient_info_list = file_list[ind + counter].split(" | ")
                    ingredients["ingredient_name"] = ingredient_info_list[0]
                    ingredients["quantity"] = int(ingredient_info_list[1])
                    ingredients["measure"] = ingredient_info_list[2]
                    all_ingredients.append(ingredients)
                    counter += 1
                    ingredient_value -= 1
                cook_book[file_list[ind - 1]] = all_ingredients
            except ValueError:
                continue

        return cook_book


def get_shop_list_by_dishes(*, dishes: list, person_count: int) -> dict:
    """
    The function increases the number of products in the recipe in proportion to the number of people
    :return: Dictionary with the number of products necessary for the preparation of all dishes from the list
    """
    cook_book = read_cook_book_from_file(file_name="cook_book.txt")
    shop_list = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_value = {k: v for k, v in ingredient.items() if k != 'ingredient_name'}
            ingredient_value["quantity"] *= person_count
            if ingredient["ingredient_name"] in shop_list:
                shop_list[ingredient["ingredient_name"]]["quantity"] += int(ingredient_value["quantity"])
            else:
                shop_list[ingredient["ingredient_name"]] = ingredient_value
    return shop_list


def reed_sort_write(*args) -> None:
    """
    The function sorts files by the number of lines of the text in them, then writes the text from them to another file
    to return the number of lines
    :return: None
    """
    result_lines_list = []
    for arg in args:
        with open(arg, "r", encoding="utf-8") as f:
            file_list = [arg, 0]
            for line in f:
                file_list[1] += 1
                file_list.append(line.strip())
            result_lines_list.append(file_list)

    result_lines_list = sorted(result_lines_list,key=len)

    with open("123.txt", "w", encoding="utf-8") as f:
        for lines in result_lines_list:
            for exem in lines:
                print_exam = str(exem) + "\n"
                f.write(print_exam)


get_shop_list_by_dishes(dishes=['Фахитос', 'Омлет'], person_count=2)
reed_sort_write("1.txt", "2.txt", "3.txt")