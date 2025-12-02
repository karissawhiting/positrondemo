library(tidyverse)

# create lil dataframe
df <- data.frame(
  x = 0:9,
  y = cumsum(rnorm(10))
)

# export dataframe
write.csv(df, "demo_data_R.csv", row.names = FALSE)

# make & save plot
png("demo_plot.png", width = 600, height = 400)
plot(df$x, df$y,
     type = "o",
     xlab = "x",
     ylab = "y",
     main = "Demo Plot")
dev.off()
