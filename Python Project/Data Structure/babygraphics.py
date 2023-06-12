"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""


import tkinter
import babynames
import babygraphicsgui as gui


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + ((width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    name_numbers = 0  # To count the number of names were entered.
    for name in lookup_names:
        name_numbers += 1
        color = COLORS[(name_numbers - 1) % len(COLORS)]  # Make each line change color.
        year_list = []  # Put rank into a list.
        rank_list = []  # Put year into a list.
        for year, rank in name_data[name].items():
            year_list.append(year)
            rank_list.append(rank)
        coordinate_y_list = []  # Put y coordinate of each text into a list.
        for i in range(len(YEARS)):
            """
            Compare the year data of entered name with ‘YEARS’,
            if it is missing, it means its rank is out of 1000,
            and replace it with '*'.
            """
            if str(YEARS[i]) not in year_list:
                rank_list.insert(i, '*')
                year_list.insert(i, '*')
            if rank_list[i] == '*':
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                                   (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) * (MAX_RANK - 1) +
                                   GRAPH_MARGIN_SIZE,
                                   text=f'{name} {rank_list[i]}', anchor=tkinter.SW, fill=color)
                coordinate_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) *\
                               (MAX_RANK - 1) + GRAPH_MARGIN_SIZE
                coordinate_y_list.append(coordinate_y)
            elif rank_list[i] != '*' and int(rank_list[i]) <= MAX_RANK:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                                   (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) *
                                   (int(rank_list[i]) - 1) + GRAPH_MARGIN_SIZE,
                                   text=f'{name} {rank_list[i]}', anchor=tkinter.SW, fill=color)
                coordinate_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / \
                               (MAX_RANK - 1) * (int(rank_list[i]) - 1) + GRAPH_MARGIN_SIZE
                coordinate_y_list.append(coordinate_y)
        for j in range(len(YEARS) - 1):
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), coordinate_y_list[j],
                               get_x_coordinate(CANVAS_WIDTH, (j + 1)), coordinate_y_list[j + 1],
                               width=LINE_WIDTH, fill=color)

    # # once the user click enter, the data will be shown
    # y_position = ((CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2)) / (MAX_RANK - 1))
    # for i in range(len(lookup_names)):
    #     # to determine the color of data's text and line
    #     if i <= len(COLORS) - 1:
    #         color = COLORS[i]
    #     else:
    #         # while the given colors are all used, the color data used will start from the first color
    #         color = COLORS[int((i % len(COLORS)))]
    #     # to find the dic of the name that contains its rank over the years
    #     baby_dic = name_data[lookup_names[i]]
    #     # to create a year list to check if the year matches the constant year list
    #     new_year_lst = []
    #     for year, rank in baby_dic.items():
    #         new_year_lst.append(year)
    #     # if the names' data doesn't exit in the given file
    #     for k in range(len(YEARS)):
    #         # assign these names' rank as 1001
    #         if f'{YEARS[k]}' not in new_year_lst:
    #             baby_dic[f'{YEARS[k]}'] = '1001'
    #     # a list that will contain the y value
    #     y_list = []
    #     for j in range(len(YEARS)):
    #         for year in baby_dic:
    #             # to find the rank of the given name in specific year
    #             rank = baby_dic[year]
    #             # to add the text of name and its rank of a specific year to the canvas
    #             line_x = get_x_coordinate(CANVAS_WIDTH, j)
    #             if int(year) == YEARS[j]:
    #                 if int(rank) > MAX_RANK:
    #                     new_rank = '*'
    #                 else:
    #                     new_rank = rank
    #                 canvas.create_text(line_x + TEXT_DX,
    #                                    int(y_position * int(rank) + GRAPH_MARGIN_SIZE),
    #                                    text=f'{lookup_names[i]} {new_rank}', anchor=tkinter.SW, fill=color)
    #                 y_list.append(int(y_position * int(rank) + GRAPH_MARGIN_SIZE))
    #     # to draw the line that connects each year's rank data on the canvas
    #     for j in range(len(YEARS) - 1):
    #         line_x = get_x_coordinate(CANVAS_WIDTH, j)
    #         line_x1 = get_x_coordinate(CANVAS_WIDTH, j + 1)
    #         line_y = y_list[j]
    #         line_y1 = y_list[j + 1]
    #         canvas.create_line(line_x, line_y, line_x1, line_y1, width=LINE_WIDTH, fill=color)

    # name_numbers = 0  # To count the number of names were entered.
    # for name in lookup_names:
    #     name_numbers += 1
    #     color = COLORS[(name_numbers - 1) % len(COLORS)]  # Make each line change color.
    #     year_list = []  # Put rank into a list.
    #     rank_list = []  # Put year into a list.
    #     for year, rank in name_data[name].items():
    #         year_list.append(year)
    #         rank_list.append(rank)
    #     coordinate_y_list = []  # Put y coordinate of each text into a list.
    #     for i in range(len(YEARS)):
    #         """
    #         Compare the year data of entered name with ‘YEARS’,
    #         if it is missing, it means its rank is out of 1000,
    #         and replace it with '*'.
    #         """
    #         if str(YEARS[i]) not in year_list:
    #             rank_list.insert(i, '*')
    #             year_list.insert(i, '*')
    #         if rank_list[i] == '*':
    #             canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
    #                                (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) * (MAX_RANK - 1) +
    #                                GRAPH_MARGIN_SIZE,
    #                                text=f'{name} {rank_list[i]}', anchor=tkinter.SW, fill=color)
    #             coordinate_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) *\
    #                            (MAX_RANK - 1) + GRAPH_MARGIN_SIZE
    #             coordinate_y_list.append(coordinate_y)
    #         elif rank_list[i] != '*' and int(rank_list[i]) <= MAX_RANK:
    #             canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
    #                                (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK - 1) *
    #                                (int(rank_list[i]) - 1) + GRAPH_MARGIN_SIZE,
    #                                text=f'{name} {rank_list[i]}', anchor=tkinter.SW, fill=color)
    #             coordinate_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / \
    #                            (MAX_RANK - 1) * (int(rank_list[i]) - 1) + GRAPH_MARGIN_SIZE
    #             coordinate_y_list.append(coordinate_y)
    #     for j in range(len(YEARS) - 1):
    #         canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), coordinate_y_list[j],
    #                            get_x_coordinate(CANVAS_WIDTH, (j + 1)), coordinate_y_list[j + 1],
    #                            width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
