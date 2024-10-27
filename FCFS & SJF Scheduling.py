from random import randint
from statistics import mean, stdev, median, mode
from scipy.stats import chi2_contingency

def FCFS(BurstTimes, Time):
    TimeNeeded = sum(BurstTimes)
    WaitingTimes = 0
    GanttChart = "\n0"
    if TimeNeeded > Time:
        TimeLoss = TimeNeeded - Time
        for Index in reversed(range(len(BurstTimes))):
            Reduction = BurstTimes[Index]
            BurstTimes[Index] -= TimeLoss
            if BurstTimes[Index]>=0:
                if BurstTimes[Index]==0:
                    BurstTimes = BurstTimes[:Index]
                else:
                    BurstTimes = BurstTimes[:Index+1]
                break
            else:
                TimeLoss -= Reduction
    
    if sum(BurstTimes)== TimeNeeded:
        Note = "IMPRESSIVE!\n"
    else:
        Note = "END IT FORCELY!\n"
        
    for Index in range(len(BurstTimes)):
        WaitingTimes += sum(BurstTimes[:Index])
        GanttChart += "-"* BurstTimes[Index] + str(sum(BurstTimes[:Index+1]))

    return [WaitingTimes, sum(BurstTimes), Note+GanttChart+"\n\nAverage Times 👇🏻\nAverage waiting time: "+str(WaitingTimes/len(BurstTimes))+"\nAverage burst time: "+str(sum(BurstTimes)/len(BurstTimes)) +"\n"+"-"*len(GanttChart)]

def SJF(BurstTimes, Time):
    return FCFS(sorted(BurstTimes), Time)

Time = int(input("How long can you wait for processes to be done? "))
if Time <= 0:
    print("Go Home, KID!")

else:
    YouOrAI = input("\nDo you want to work with unknown processes? (Y, N) ")
    while YouOrAI not in ["Y", "N"]:
        YouOrAI = input("Do you want to work with unknown processes? (Y, N) ")
    
    if YouOrAI == "N":
        print("You decide what would happen\n")
        NumberOfProcesses = int(input("How many processes are there for being burst? "))
        BurstTimes = [0] * NumberOfProcesses
        for Index in range(NumberOfProcesses):
            BurstTimes[Index] = int(input("How long does "+str(Index+1)+ "th process takes to be done? "))
        print("\nBy FCFS algorithm we have:")
        print(FCFS(BurstTimes, Time)[2])
        print("By SJF algorithm we have:")
        print(SJF(BurstTimes, Time)[2])
        
    else:
        print("Some unknown processes are coming..!\n")
        NumberOfExperiences = int(input("How many times do you want to run the algorithm? Choose from range (30, 1000) "))
        while 30 > NumberOfExperiences or NumberOfExperiences > 1000:
            NumberOfExperiences = int(input("I Told you choose from range (30, 1000) "))
        TotalWaitingTimesFCFS=[]
        TotalWaitingTimesSJF=[]
        TotalBurstTimes=[]
        for Experience in range(NumberOfExperiences):
            NumberOfProcesses = randint(1, 1000)
            BurstTimes = []
            for Index in range(NumberOfProcesses):
                BurstTimes.append(randint(1, 1000))   
            OutputDatas=FCFS(BurstTimes, Time)[:2]
            TotalWaitingTimesFCFS.append(OutputDatas[0])
            TotalBurstTimes.append(OutputDatas[1])
            TotalWaitingTimesSJF.append(SJF(BurstTimes, Time)[0])

        print("\nHere's the statistical quantities 👇🏻")
        print("Waiting Times:")
        print("\nMean of the whole waiting times of the random processes obtained of FCFS algorithm is", mean(TotalWaitingTimesFCFS))
        print("\nMedian of the whole waiting times of the random processes obtained of FCFS algorithm is", median(TotalWaitingTimesFCFS))
        print("\nMode Deviation of the whole waiting times of the random processes obtained of FCFS algorithm is", mode(TotalWaitingTimesFCFS))
        print("\nStandard Deviation of the whole waiting times of the random processes obtained of FCFS algorithm is", stdev(TotalWaitingTimesFCFS))
        print("\nMean of the whole waiting times of the random processes obtained of SJF algorithm is ", mean(TotalWaitingTimesSJF))
        print("\nMedian of the whole waiting times of the random processes obtained of SJF algorithm is ", median(TotalWaitingTimesSJF))
        print("\nMode Deviation of the whole waiting times of the random processes obtained of SJF algorithm is", mode(TotalWaitingTimesSJF))
        print("\nStandard Deviation of the whole waiting times of the random processes obtained of SJF algorithm is", stdev(TotalWaitingTimesSJF))
        print("\nBurst Times:")
        print("\nMean of the whole burst times of the random processes obtained of both algorithms is", mean(TotalBurstTimes))
        print("\nMedian of the whole burst times of the random processes obtained of both algorithms is", median(TotalBurstTimes))
        print("\nMode Deviation of the whole burst times of the random processes obtained of both algorithms is", mode(TotalBurstTimes))
        print("\nStandard Deviation of the whole burst times of the random processes obtained of both algorithms is", stdev(TotalBurstTimes))
    print("\nHave a nice day😘")
