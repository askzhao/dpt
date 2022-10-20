import  xml.dom.minidom

dom = xml.dom.minidom.parse('dimens.xml')

root = dom.documentElement
for node in root.childNodes:
    # print(node.nodeName+root.nodeValue)
    if node.childNodes.length <= 0:
        continue
    dp = node.childNodes[0].data
    print(dp)
    sdp = dp.replace("dp","")
    print(sdp)
    nDp = (float(sdp))/2.63
    print(nDp)
    node.childNodes[0].data = str(nDp)+"dp"

fp = open('dimens2.xml', 'w', encoding='utf-8')
dom.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()

