x="""03/17/2022,292.73,294.92,288.7,294.69,20827966
03/18/2022,293.71,300.3,292.06,299.81,33586950
03/21/2022,298.15,299.44,294.21,298.47,20156097
03/22/2022,298.98,304.29,298.08,303.46,19022258
03/23/2022,299.98,302.53,297.03,298.71,19163830
03/24/2022,299.01,303.49,297.62,303.4,16505550
03/25/2022,304.52,304.79,298.59,302.98,16503912
03/28/2022,303.54,310.08,303.54,310.04,21181093
03/29/2022,312.95,315.09,308.33,314.69,22774000
03/30/2022,312.98,315.22,310.86,313.33,19203780
03/31/2022,313.28,314.41,307.17,307.36,26084298
04/01/2022,308.74,309.41,304.83,308.7,19656973
04/04/2022,309.37,314.38,308.99,314.34,18262400
04/05/2022,312.55,314.14,309.15,310.29,17900901
04/06/2022,304.48,306.29,296.02,298.7,30240701
04/07/2022,295.97,302.94,295.66,300.8,23139149
04/08/2022,299.74,300.42,295.59,296.31,17901519
04/11/2022,291.09,291.93,284.34,284.6,26474036
04/12/2022,288.6,290.06,279.84,281.33,23155555
04/13/2022,282.07,287.91,280.65,286.93,16671889
04/14/2022,287.42,287.64,278.68,279.13,20964140
04/18/2022,278.34,281.8,277.69,279.95,15761342
04/19/2022,278.73,285.51,277.76,284.72,16199280
04/20/2022,288.67,289.03,284.67,285.66,16466986
04/21/2022,287.77,292.62,279.41,280.16,21697127
04/22/2022,281.31,282.54,272.74,273.39,21065338
04/25/2022,272.65,280.46,270.14,280.11,25969060
04/26/2022,276.86,277.71,269.37,269.59,32552977
04/27/2022,281.63,290.29,278.51,282.42,46924336
04/28/2022,284.52,290.3,280.8,289.05,23986952
04/29/2022,287.74,289.21,275.86,276.9,26787190
05/02/2022,277.02,284.28,275.58,283.94,25039209
05/03/2022,283.3,283.47,279.5,281.18,17113675
05/04/2022,281.94,290.2,276.09,289.36,24342229
05/05/2022,285.12,285.68,273.7,276.88,32150648
05/06/2022,274.18,278.6,270.64,274.09,26074640
05/09/2022,269.38,271.73,262.71,263.98,33120265
05/10/2022,270.98,273.11,264.45,268.82,27336965
05/11/2022,265.19,270.73,258.7,260.05,30802726
05/12/2022,257.03,259.28,249.44,254.78,35522614
05/13/2022,256.75,262.43,254.76,260.46,24993911
05/16/2022,259.39,265.2,255.19,260.93,24373240
05/17/2022,265.52,267.71,261.85,266.24,21253594
05/18/2022,263,263.6,252.77,254.14,23907379
05/19/2022,253.89,257.67,251.88,253.13,23351671
05/20/2022,257.41,258.54,246.44,252.56,28620671
05/23/2022,255.85,261.5,253.43,260.65,24665116
05/24/2022,257.87,261.33,253.5,260,22021907
05/25/2022,258.14,264.58,257.125,262.66,20901035
05/26/2022,262.27,267.11,261.4294,265.86,18704678
05/27/2022,268.51,273.34,267.56,273.23,20440638
05/31/2022,272.49,274.77,268.93,271.98,26176882
06/01/2022,275.195,277.69,270.04,272.35,18917683
06/02/2022,264.45,274.65,261.6,274.63,33733826
06/03/2022,270,273.45,268.41,270.05,18023130
06/06/2022,272.06,274.18,267.22,268.75,14877558
06/07/2022,266.57,273.13,265.94,272.5,15160802
06/08/2022,271.76,273,269.61,270.46,12964736
06/09/2022,267.78,272.7081,264.63,264.7,17799380
06/10/2022,260.42,260.58,252.53,252.89,23374092
06/13/2022,245.16,249.0242,241.53,242.33,31308306
06/14/2022,243.83,245.74,241.51,244.5676,20455769
06/15/2022,248.3,255.3,246.42,251.76,25063169
06/16/2022,246.08,247.4174,243.02,245.11,24851739
06/17/2022,244.53,250.5,244.03,247.53,33839808
06/21/2022,250.255,254.75,249.51,253.74,19719699
06/22/2022,251.99,257.17,250.37,253,18632295
06/23/2022,255.57,259.37,253.63,258.92,18568206
06/24/2022,261.81,267.98,261.72,267.98,26084538"""
print(x)
words=x.split()
print(words)
for w in words:
    e=w.split(",")
    for p in e:
        print(p,end=" ")
    print()
#7788 scott 3000.00
#7369 blake 4000.00
#7902 smith 3500.00
