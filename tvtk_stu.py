import vtk 
# from tvtk.api import tvtk 

# 创建一个圆锥体数据对象 
cone = vtk.vtkConeSource() 

# 创建一个Poly数据对象进行显示 
coneMapper = vtk.vtkPolyDataMapper() 
coneMapper.SetInputConnection(cone.GetOutputPort()) 

# 创建Actor并设置Mapper 
coneActor = vtk.vtkActor() 
coneActor.SetMapper(coneMapper) 

# 创建渲染器和窗口 
renderer = vtk.vtkRenderer() 
renderWindow = vtk.vtkRenderWindow() 
renderWindow.AddRenderer(renderer) 

# 创建交互器和窗口 
interactor = vtk.vtkRenderWindowInteractor() 
interactor.SetRenderWindow(renderWindow) 

# 将圆锥体Actor添加到渲染器中 
renderer.AddActor(coneActor) 

# 开始交互式渲染并等待窗口关闭 
renderWindow.Render() 
interactor.Start()  