import recordvoice
import mainstt
import text_localization
import mouseByKeyboard 
cond = True
while cond == True:
    condition = mouseByKeyboard.start()

    if condition != False:
        recordvoice.record()
        mainstt.stt()
        coords1 = text_localization.scan()
        cond = mouseByKeyboard.coordenates(coords1[0], coords1[1], coords1[2], coords1[3])
