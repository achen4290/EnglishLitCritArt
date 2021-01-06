# Artistic Representation of a Lit Crit
Made by Andrew Chen for Mrs. Martin's Pd4 "English 12 AP" class.

## Goal
I was inspired by the [Brain Games intro](https://www.youtube.com/watch?v=P7PCaoh_Ba0) to automate the process of creating a 3D work of art that looks completely different depending on the viewing angle.

## The actual project
There are two main components to the project
1. Grid editor
2. Grid plotter

### Grid editor
The grid editor is accessed by running the "main_editor" file. It looks like this:

![Grid editor screenshot](https://cdn.discordapp.com/attachments/734540453541838969/796514073122439238/Screen_Shot_2021-01-06_at_6.02.28_PM.png)

The concept is that you get to draw on each of the 18x18 canvases what you want the final product to look like from a certain angle

There are 2 buttons for each canvas: 
1. Clear (clears the canvas)
1. Fill (fills the entire canvas)

There are also two buttons at the bottom of the entire window:
1. Pixelate (The final object is rendered by a bunch of cubes, so this button pixelates your drawing so you can see exactly what to expect in the final product.
2. Save (Saves your drawings and closes the grid editor)

Each of the 3 views (XZ, YZ, XY) represent what it will look like if you view the 3D object from a location perpendicular to that plane.

### Grid plotter
The grid plotter is accessed by running the "main_plotter" file. It looks like this:

![Grid plotter screenshot](https://cdn.discordapp.com/attachments/734540453541838969/796516197692473414/Screen_Shot_2021-01-06_at_6.10.53_PM.png)

It is simply a menu to choose which grid you want to plot. You should see 4 grids in the menu:
1. Faces (happy face, sad face, and surprised face)
2. Shapes (circle, rectangle, and triangle)
3. Brain Games (One view is BRAIN, one view is GAMES, and there is no XY view)
4. Most Recent Save (Your most recently saved grid using the grid editor)

Clicking on any of the options and then the "Display Plot" button will close the menu and open up a 3D plotly plot in a browser window. It should look something like this:

![plotly screenshot](https://cdn.discordapp.com/attachments/734540453541838969/796517457946214470/Screen_Shot_2021-01-06_at_6.15.57_PM.png)

You can click and drag to rotate the figure to view it from all 3 angles (see the gif below!)

![brain games gif](https://cdn.discordapp.com/attachments/734540453541838969/796518520510480434/brain_games.gif)

