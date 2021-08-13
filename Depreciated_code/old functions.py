# old function for transformation, new to come
"""def transform_pixel_to_mm(dist_px):
    x1 = 47
    x2 = 566
    y1 = 0
    y2 = 1000
    a = (y1 - y2) / (x1 - x2)
    b = int(y2 - a * x2)
    dist_mm = round(a * dist_px + b)
    return dist_mm


def flip_x_axis(y_coord_cam):
    x1 = 0
    x2 = 1000
    y1 = 1000
    y2 = 0
    a = (y1 - y2) / (x1 - x2)
    b = y2 - a * x2
    new_x_coord = round(a * y_coord_cam + b)
    return new_x_coord


def flip_y_axis(x_coord_cam):
    x1 = 0
    x2 = 1500
    y1 = 0
    y2 = 1500
    a = (y1 - y2) / (x1 - x2)
    b = y2 - a * x2
    new_y_coord = round(a * x_coord_cam + b)
    return new_y_coord"""

# Creates the SVG file using the old transform to real world coordinates
        """sheet = svg.Drawing('sheet.svg')
        for cnt in contours:
            for i in range(len(cnt) - 1):
                sheet.add(sheet.line(
                    (
                    flip_x_axis(transform_pixel_to_mm(cnt[i][0][1])), flip_y_axis(transform_pixel_to_mm(cnt[i][0][0]))),
                    (
                        flip_x_axis(transform_pixel_to_mm(cnt[i + 1][0][1])),
                        flip_y_axis(transform_pixel_to_mm((cnt[i + 1][0][0])))), stroke=svg.rgb(0, 0, 0, '%')))
            sheet.add(sheet.line(
                (flip_x_axis(transform_pixel_to_mm(cnt[0][0][1])), flip_y_axis(transform_pixel_to_mm(cnt[0][0][0]))), (
                    flip_x_axis(transform_pixel_to_mm(cnt[-1][0][1])),
                    flip_y_axis(transform_pixel_to_mm((cnt[-1][0][0])))), stroke=svg.rgb(0, 0, 0, '%')))"""