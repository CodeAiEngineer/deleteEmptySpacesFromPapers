# deleteEmptySpacesFromPapers
delete Empty Spaces From Papers


It corrects incorrect spaces, especially when copying text from PDF files. Copy the text to the TXT file and then run the code. 



Example wrong text with incorrect spaces:

4.1 3D Best Fit Algorithm
Decide on a packing direction. Each bin has three
directions in which to pack, a width (or x) direction, a
height (or y) direction, a depth (or z) direction. pack one
bin at a time.
We first choose a pivot point. The pivot is an (x, y, z)
coordinate which represents a point in a particular 3D bin
at which an attempt to pack an item will be made. the
back lower left corner of the item will be placed at the
pivot. If the item cannot be packed at the pivot position
then it is rotated until it can be packed at the pivot point
or until we have tried all 6 possible rotation types. If after
rotating it, the item still cannot be packed at the pivot
point, then we move on to packing another item and add
the unpacked item to a list of items that will be packed
after an attempt to pack the remaining items is made. the
first pivot in an empty bin is always (0,0,0).
