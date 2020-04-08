from random import randint

#Generates job.txt where num_jobs is the number of jobs in the file
#Jobs generated will have values in the range [low,high]
def generate_job_file(num_jobs, low, high):
    with open("job.txt", "w") as jobs:
        for i in range(num_jobs):
            jobs.write("Job{}\n{}\n".format(i+1, randint(low, high)))


#reads the job file and returns a list of values of all the jobs
def read_job_file():
    dct = {}
    with open("job.txt", "r") as jobs:
        #reads jobs file and turns it into a dict of every line in the file as an entry
        #afterwards, deletes newline characters in every entry in list using replace()
        jobs_lst = [j.replace("\n", "") for j in jobs.readlines()]

        for i in range(0, len(jobs_lst), 2):
            dct[jobs_lst[i]] = int(jobs_lst[i+1])

    return dct


#First-Come-First-Serve
def fcfs(data, show_steps=False):
    #uses fact that python 3 dictionaries keep insertion order

    time = 0
    total_time = 0
    prev_add = 0
    num_turnaround = len(data)

    for k, v in data.items():
        if show_steps:
            print("Starting {} at time {}".format(k, time))
            time += v
            print("Ending {} at time {}".format(k, time))
        
        total_time += (prev_add + v)
        prev_add += v

    return total_time/num_turnaround


#Shortest-Job-First(SJF)
def sjf(data, show_steps=False):
    #FCFS but with the data sorted ascending by the times
    return fcfs({k: v for k, v in sorted(data.items(), key=lambda x: x[1])}, show_steps)


#Round-Robin with input time slice
def rr(data, time_slice, show_steps=False):
    copy = data.copy()
    time = 0
    total_time = 0
    num_turnaround = len(data)

    while True:
        #will keep going until it finds that none of the values have been changed, which is when all jobs are done
        changed = False
        for k, v in copy.items():
            if v == 0:
                continue

            if show_steps:
                print("Starting {} at time {}".format(k, time))
            
            if v <= time_slice:
                time += v
                copy[k] = 0
                total_time += time
                changed = True

                if show_steps:
                    print("   Finished {} at time {}".format(k, time))
            else:
                time += time_slice
                copy[k] -= time_slice
                changed = True

                if show_steps:
                    print("Ending   {} at time {}".format(k, time))

        if not changed:
            break
                
    return total_time/num_turnaround



if __name__ == "__main__":
    
    num_trials = 20
    num_jobs_list = [5, 10, 15]
    
    low = 1
    high = 30

    print("Range of values: [{},{}]\n".format(low, high))

    for n in num_jobs_list:
        fcfs_avg = 0
        sjf_avg = 0
        rr_2_avg = 0
        rr_5_avg = 0

        for _ in range(num_trials):

            generate_job_file(n, low, high)
            data = read_job_file()
            
            fcfs_avg += fcfs(data)
            sjf_avg += sjf(data)
            rr_2_avg += rr(data, 2)
            rr_5_avg += rr(data, 5)

        fcfs_avg /= num_trials 
        sjf_avg /= num_trials  
        rr_2_avg /= num_trials 
        rr_5_avg /= num_trials 

        print("FCFS Average over {} trials with {} jobs: {}".format(num_trials, n, fcfs_avg))
        print("SJF  Average over {} trials with {} jobs: {}".format(num_trials, n, sjf_avg))
        print("RR 2 Average over {} trials with {} jobs: {}".format(num_trials, n, rr_2_avg))
        print("RR 5 Average over {} trials with {} jobs: {}".format(num_trials, n, rr_5_avg))
        print("-------------------------------------------------------------------------------")


    #test code

    #generate_job_file(5, 1, 30)
    #jobs = read_job_file()
    #print("Number of jobs: ", len(jobs))
    #print("FCFS: ", fcfs(jobs, True))
    #print("SJF: ", sjf(jobs, True))
    #print("RR (Time Slice 2): ", rr(jobs, 2, True))
    #print("RR (Time Slice 5): ", rr(jobs, 5, True))
