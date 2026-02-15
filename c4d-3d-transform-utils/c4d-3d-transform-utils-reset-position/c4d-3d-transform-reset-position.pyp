import c4d,os
PLUGIN_ID = 1067534
class ResetPositionCommand(c4d.plugins.CommandData):
    def Execute(self, doc):
        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        doc.StartUndo()
        
        for obj in objects:
            new_matrix = obj.GetMl()
            new_matrix.off = c4d.Vector(0.0)
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            obj.SetMl(new_matrix) 
        doc.EndUndo()
        c4d.EventAdd()
        return True

if __name__=='__main__':
    bmp  = c4d.bitmaps.BaseBitmap()
    dir,f=os.path.split(__file__)
    fn   =os.path.join(dir,"res\icons","icon.png")
    bmp.InitWith(fn)
    register = c4d.plugins.RegisterCommandPlugin( id  =PLUGIN_ID,
                                                 str  ="Reset Position",
                                                 help ="JhoelRm",
                                                 info =c4d.PLUGINFLAG_COMMAND_STICKY,
                                                 dat  =ResetPositionCommand(),
                                                 icon =bmp )
    if register:
        print ("Plugin [Reset Position] registered successfully.")
    else:
        print ("Plugin [Reset Position] registration failed.")