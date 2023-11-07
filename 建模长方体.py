import vtk
# 1. 读取数据
cube = vtk.vtkCubeSource()
cube.Update()#记得加这句不加看不到模型
# 2. 建图（将点拼接成立方体）
cube_mapper = vtk.vtkPolyDataMapper()
cube_mapper.SetInputData(cube.GetOutput())
# 3. 根据2创建执行单元
cube_actor = vtk.vtkActor()
cube_actor.SetMapper(cube_mapper)
 
cube_actor.GetProperty().SetColor(1.0, 0.0, 0.0)
# 4. 渲染（将执行单元和背景组合在一起按照某个视角绘制）
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)#背景只有一个所以是Set()
renderer.AddActor(cube_actor)#因为actor有可能为多个所以是add()
 
# 5. 显示渲染窗口
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("My First Cube")
render_window.SetSize(400,400)
render_window.AddRenderer(renderer)# 渲染也会有可能有多个渲染把他们一起显示
# 6. 创建交互控键（可以用鼠标拖来拖去看三维模型）
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)
interactor.Initialize()
render_window.Render()
interactor.Start()
