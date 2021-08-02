import ezdxf

line_color = {'color': 7}
doc = ezdxf.new(dxfversion='R2010')
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})
msp = doc.modelspace()

point_list_start = 0
point_list = [(155, 53), (462, 500), (769, 52)]

# point_file = open("main_copytst2_contours.txt", "r")

with open("main_copytst2_contours.txt","r") as point_file:
    filter = point_file.read()
    filter = filter.replace(" ", "").replace("\n\n", "\n")
    filter = filter.replace("array([" , "").replace("dtype" , "")
    filter = filter.replace("int32", "").replace(",=)", "")
    filter = filter.replace("[[", "").replace("]],\n",",").replace("]]]","")

lines_list  = filter.split(",")
point_list2 = ([int(x) for x in lines_list])




counter_stop = (len(point_list) - 1)
point_a = -1
point_b = 0

while True:
    point_a = point_a + 1
    point_b = point_b + 1
    # print(point_list[point_a], point_list[point_b])
    msp.add_line(point_list[point_a], point_list[point_b], line_color)
    if point_b == counter_stop:
        # print(point_list[point_b], point_list[0])
        msp.add_line(point_list[point_b], point_list[0], line_color)
        break

# msp.add_line(point_0, point_1, line_color)
# msp.add_line(point_1, point_2, line_color)
# msp.add_line(point_2, point_0, line_color)
msp.add_text(
    'Table Test',
    dxfattribs={
        'layer': 'TEXTLAYER'
    }).set_pos((0, 0.2), align='CENTER')

doc.saveas('test.dxf')
point_file.close()
