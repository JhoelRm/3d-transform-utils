import c4d,os,math
PLUGIN_ID = 1067535

class ResetRotationCommand(c4d.plugins.CommandData):
    def Execute(self, doc):

        def NormalizeAngle(angle):
            while angle > math.pi:
                angle -= 2 * math.pi
            while angle < -math.pi:
                angle += 2 * math.pi
            return angle
        
        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        doc.StartUndo()

        for obj in objects:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

            new_matrix = obj.GetMl()

            new_matrix.v1 = c4d.Vector(new_matrix.v1.GetLength(), 0, 0)
            new_matrix.v2 = c4d.Vector(0, new_matrix.v2.GetLength(), 0)
            new_matrix.v3 = c4d.Vector(0, 0, new_matrix.v3.GetLength())

            obj.SetMl(new_matrix)
            
            rot = obj.GetRelRot()
            rot.x = NormalizeAngle(rot.x)
            rot.y = NormalizeAngle(rot.y)
            rot.z = NormalizeAngle(rot.z)
            obj.SetRelRot(rot)

        doc.EndUndo()
        c4d.EventAdd()
        return True

if __name__=='__main__':
    bmp  = c4d.bitmaps.BaseBitmap()
    dir,f=os.path.split(__file__)
    fn   =os.path.join(dir,"res\icons","icon.png")
    bmp.InitWith(fn)
    register = c4d.plugins.RegisterCommandPlugin( id  =PLUGIN_ID,
                                                 str  ="Reset Rotation",
                                                 help ="JhoelRm",
                                                 info =c4d.PLUGINFLAG_COMMAND_STICKY,
                                                 dat  =ResetRotationCommand(),
                                                 icon =bmp )
    if register:
        print ("Plugin [Reset Rotation] registered successfully.")
    else:
        print ("Plugin [Reset Rotation] registration failed.")