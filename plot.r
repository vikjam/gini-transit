library(acs)
library(ggplot2)

mbta_data        <- read.csv("mbta.csv", header = FALSE, stringsAsFactors = FALSE)
names(mbta_data) <- c("color", "line", "station", "longitude", "latitude", "block")
mbta_data$tract  <- as.numeric(substr(mbta_data$block, 1, 14))
tracts           <- unique(mbta_data$tract)

# End of the script
