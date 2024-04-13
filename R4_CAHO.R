grade<-final_data$grade
breaks <- seq(min(grade), max(grade)+1, length.out = 13)
# Save as JPG
jpeg(filename = "grade_distribution.jpg", width = 800, height = 500)
h<-hist(grade, 
        main="Distribución de las calificaciones.", 
        xlab="Calificación", 
        ylab="Frecuencia", 
        col="#99FFFF", 
        border="black",
        breaks=breaks)
text(h$mids,h$counts,labels=h$counts, adj=c(0.5, -0.5))

dev.off()

tabla_frecuencias <- cut(grade, breaks = breaks, include.lowest = TRUE, right = FALSE)

df <- as.data.frame(table(tabla_frecuencias))

# Exportar a CSV
write.csv(df, "tabla_frecuencias.csv", row.names = FALSE)



print(table(tabla_frecuencias))
