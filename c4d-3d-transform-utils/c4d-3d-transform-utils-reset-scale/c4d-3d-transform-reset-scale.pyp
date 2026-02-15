import c4d,os
PLUGIN_ID = 1067536

class ResetScaleCommand(c4d.plugins.CommandData):
    def Execute(self, doc):

        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        doc.StartUndo()

        for obj in objects:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

            m = obj.GetMl()
            
            m.v1 = m.v1.GetNormalized()
            m.v2 = m.v2.GetNormalized()
            m.v3 = m.v3.GetNormalized()

            obj.SetMl(m)

        doc.EndUndo()
        c4d.EventAdd()
        return True

if __name__=='__main__':
    bmp  = c4d.bitmaps.BaseBitmap()
    dir,f=os.path.split(__file__)
    fn   =os.path.join(dir,"res\icons","icon.png")
    bmp.InitWith(fn)
    register = c4d.plugins.RegisterCommandPlugin( id  =PLUGIN_ID,
                                                 str  ="Reset Scale",
                                                 help ="JhoelRm",
                                                 info =c4d.PLUGINFLAG_COMMAND_STICKY,
                                                 dat  =ResetScaleCommand(),
                                                 icon =bmp )
    if register:
        print ("Plugin [Reset Scale] registered successfully.")
    else:
        print ("Plugin [Reset Scale] registration failed.")