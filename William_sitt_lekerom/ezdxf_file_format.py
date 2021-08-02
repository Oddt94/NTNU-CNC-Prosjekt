import ezdxf

line_color = {'color': 7}
doc = ezdxf.new(dxfversion='R2010')
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})
msp = doc.modelspace()

# point_file = open("main_copytst2_contours.txt", "r")

with open("main_copytst3_contours.txt", "r") as point_file:
    filter = point_file.read()
    filter = filter.replace(" ", "").replace("\n\n", "\n")
    filter = filter.replace("array([", "").replace("dtype", "")
    filter = filter.replace("int32", "").replace(",=)", "")
    filter = filter.replace("[[", "").replace("]],\n", ",").replace("]]]", "")

lines_list = filter.split(",")
point_list2 = ([int(x) for x in lines_list])
counter_stop = (len(point_list2) / 2)
counter = 1
pl2 = point_list2
i = 0

while True:
    counter = counter + 1
    point_a = (pl2[i+0], pl2[i+1])
    point_b = (pl2[i+2], pl2[i+3])
    msp.add_line(point_a, point_b, line_color)
    i = i + 2
    if counter >= counter_stop:
        point_a = (pl2[i], pl2[i+1])
        point_b = (pl2[i-i], pl2[i-i-1])
        msp.add_line(point_a, point_b, line_color)
        break
msp.add_text(
    'Table Test',
    dxfattribs={
        'layer': 'TEXTLAYER'
    }).set_pos((0, 0.2), align='CENTER')

doc.saveas('test.dxf')
point_file.close()
