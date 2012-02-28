### Reading in data###
SomaliAid = read.csv("Famine in Somalia%3A how did the world respond%3F DATA - Aid flows.csv", header = TRUE, sep = ",", quote="\"", dec=".", fill = TRUE, comment.char="")

#Converting date column to date type#
SomaliAid$Date = as.Date(SomaliAid$Decision.date, format = "%m/%d/%Y")

#Making a new column of just the categories#
for(row in 1:594){
	for(col in 6:16){
		if(!is.na(SomaliAid[col][row,])){
			SomaliAid$category[row] = names(SomaliAid)[col]
		}
	}
}

#Pivoting donations by day and category
categoryDonationsByDay = aggregate(SomaliAid$USD.committed..contributed, list(category = SomaliAid$category, Date = SomaliAid$Date), sum)

#Reforming the category columns to fit the visualisation
library("reshape")
donorDonationsByDay = cast(categoryDonationsByDay, Date ~ category, add.missing = 0)

#Writing it to csv with 0 as NA
write.csv(donorDonationsByDay, "DonorDonationsByDay.csv", row.names = F, na = "0")

