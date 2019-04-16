cbf1 = read.table("CBF1/CBF1_peaks.broadPeak", sep = "\t")
rcm1 = read.table("RCM1/RCM1_peaks.broadPeak", sep = "\t")

names(cbf1) = c("Chr", "start", "end", "peak", "reads", "strand", 
               "Signal.Value", "P.value", "qvalue")
names(rcm1) = c("Chr", "start", "end", "peak", "reads", "strand", 
                "Signal.Value", "P.value", "qvalue")

cbf1 = cbf1[cbf1$qvalue > 5,]
rcm1 = rcm1[rcm1$qvalue > 5,]

dir.create("figures")

length.his = function(dat, name)   {
  dat$range = dat$end - dat$start
  setEPS()
  postscript(paste("figures/", name, "peak length.eps"), width = 7, height = 5)
  
  hist(dat$range[dat$range<5000], breaks = 100, main = name, 
       ylab = "number of peaks", xlab = "size of peaks", col = "grey80")
  dev.off()
  
  }

length.his(cbf1, "cbf1")
length.his(rcm1, "rcm1")


CBF1 = as.vector(cbf1$peak)
rcm1.c = merge(rcm1, d1, by.x = "peak", by.y = "overlap", all.x = T)
rcm1.c$peak = as.character(rcm1.c$peak)
rcm1.c$RC = as.character(rcm1.c$peak.cbf)
rcm1.c$RC[is.na(rcm1.c$peak.cbf)] <- rcm1.c$peak[is.na(rcm1.c$peak.cbf)]
RCM1 = as.character(rcm1.c$RC)

input  <-list(CBF1, RCM1)

names(input) = c("CBF1", "RCM1")

require(VennDiagram)

tiff("figures/venn diagram cbf1 rcm1.tiff", width = 500, height = 500, units = "px")
vp <- venn.diagram(input, fill = 2:4, alpha = 0.3, filename = NULL, scaled = 3, resolution = 300);
grid.draw(vp)
dev.off()







