import time
import random

# --- Mock Agent Functions ---
def profile_agent(user_profile):
    print("[Profile Agent] Extracting skills from resume...")
    time.sleep(1)
    return {
        "skills": user_profile["skills"],
        "experience": user_profile["experience"]
    }

def assessment_agent(skills):
    print("[Assessment Agent] Generating adaptive questions...")
    time.sleep(1)
    return {skill: random.randint(60, 90) for skill in skills}

def recommender_agent(scores):
    print("[Recommender Agent] Analyzing skill gaps and suggesting modules...")
    time.sleep(1)
    modules = []
    for skill, score in scores.items():
        if score < 80:
            modules.append({"module": f"Improve {skill}", "time": f"{random.randint(4, 8)}h"})
    return modules

def tracker_agent(modules):
    print("[Tracker Agent] Tracking learning modules and progress...")
    time.sleep(1)
    return [f"Not Started: {m['module']}" for m in modules]

def hackathon_agent():
    print("[Hackathon Agent] Setting up upcoming hackathon...")
    time.sleep(1)
    return {
        "title": "AI in Education",
        "start_date": "2025-06-10",
        "challenges": [
            "Build an AI tutor bot",
            "Classify student performance data",
            "Generate quiz questions using LLMs"
        ]
    }

# --- Main CLI Simulation ---
user_profile = {
    "name": "Jayesh",
    "skills": ["Python", "SQL", "React"],
    "experience": "2 years"
}

def print_progress_bar():
    steps = ["Profile Created", "Assessment Completed", "Skills Evaluated", "Learning Path Generated", "Hackathon Joined"]
    for i, step in enumerate(steps):
        print(f"[{'■'*(i+1)}{'□'*(len(steps)-i-1)}] {step}")
        time.sleep(0.4)

def main():
    print("\n🔹 Welcome to Forge – Your Personalized Coding Mentor\n")
    time.sleep(1)

    # Profile Agent
    profile = profile_agent(user_profile)
    print(f"✅ Skills Extracted: {', '.join(profile['skills'])}")
    print(f"📊 Experience Level: {profile['experience']}")

    # Assessment Agent
    scores = assessment_agent(profile["skills"])
    for skill, score in scores.items():
        print(f"✔️ {skill} Score: {score}%")

    # Recommender Agent
    modules = recommender_agent(scores)
    for m in modules:
        print(f"📚 Suggested: {m['module']} ({m['time']})")

    # Tracker Agent
    progress = tracker_agent(modules)
    for p in progress:
        print(f"🔄 {p}")

    # Hackathon Agent
    hackathon = hackathon_agent()
    print(f"🚀 Upcoming Hackathon: {hackathon['title']} on {hackathon['start_date']}")
    for ch in hackathon["challenges"]:
        print(f"   - {ch}")

    print("\n🎯 Your Progress:")
    print_progress_bar()

    print("\n🏁 Commands:")
    print(" - `forge learn` to start learning")
    print(" - `forge hackathon` to view or join a challenge")
    print(" - `forge status` to see your progress")

if __name__ == "__main__":
    main()
