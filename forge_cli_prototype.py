import time
import random
import sys

# --- User Profile ---
user_profile = {
    "name": "Jayesh",
    "skills": ["Python", "SQL", "React"],
    "experience": "2 years"
}

# --- Agent Logic ---
def profile_agent():
    print("[Profile Agent] Extracting skills and experience...")
    time.sleep(1)
    return user_profile

def assessment_agent(skills):
    print("[Assessment Agent] Running adaptive assessment...")
    time.sleep(1)
    return {skill: random.randint(60, 95) for skill in skills}

def recommender_agent(scores):
    print("[Recommender Agent] Generating learning recommendations...")
    time.sleep(1)
    modules = []
    for skill, score in scores.items():
        if score < 80:
            modules.append({"module": f"Mastering {skill}", "time": f"{random.randint(4, 8)}h"})
    return modules

def tracker_agent(modules):
    print("[Tracker Agent] Tracking module progress...")
    time.sleep(1)
    return {module["module"]: "Not Started" for module in modules}

def hackathon_agent():
    print("[Hackathon Agent] Preparing hackathon info...")
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

def print_progress_bar():
    steps = ["Profile Created", "Assessment Completed", "Skills Evaluated", "Learning Path Generated", "Hackathon Joined"]
    for i, step in enumerate(steps):
        print(f"[{'■'*(i+1)}{'□'*(len(steps)-i-1)}] {step}")
        time.sleep(0.3)

# --- CLI Commands ---
def forge_main():
    print("\n🔹 Welcome to Forge – Your Personalized Coding Mentor\n")

    profile = profile_agent()
    print(f"✅ Name: {profile['name']}, Experience: {profile['experience']}")
    print(f"✅ Skills: {', '.join(profile['skills'])}")

    scores = assessment_agent(profile['skills'])
    print("\n📊 Assessment Results:")
    for skill, score in scores.items():
        print(f" - {skill}: {score}%")

    modules = recommender_agent(scores)
    print("\n📚 Recommended Learning Modules:")
    for m in modules:
        print(f" - {m['module']} ({m['time']})")

    progress = tracker_agent(modules)
    print("\n🔄 Learning Tracker:")
    for module, status in progress.items():
        print(f" - {module}: {status}")

    hackathon = hackathon_agent()
    print(f"\n🚀 Upcoming Hackathon: {hackathon['title']} (Starts: {hackathon['start_date']})")
    for ch in hackathon['challenges']:
        print(f"   • {ch}")

    print("\n🎯 Progress Overview:")
    print_progress_bar()

    print("\n🏁 Try commands: \n - python forge.py learn\n - python forge.py hackathon\n - python forge.py status")


def forge_learn():
    print("\n📘 Starting Learning Session...\n")
    print("Modules in progress: React, SQL Optimization")
    time.sleep(1)
    print("✅ Tips: Break problems into smaller pieces. Practice daily.\n")

def forge_hackathon():
    print("\n🚧 Hackathon Zone\n")
    print("- You are registered for: AI in Education")
    print("- Challenge: Build an AI tutor that adapts to student progress")
    print("💡 Tip: Use GPT prompts to simulate questions based on difficulty")


def forge_status():
    print("\n📈 Current Status\n")
    print(" - Assessments: Completed")
    print(" - Modules: 2 pending")
    print(" - Hackathon: Joined")
    print("🎖️ Keep going, you're doing great!\n")

# --- Main Entrypoint ---
if __name__ == '__main__':
    if len(sys.argv) == 1:
        forge_main()
    else:
        cmd = sys.argv[1]
        if cmd == 'learn':
            forge_learn()
        elif cmd == 'hackathon':
            forge_hackathon()
        elif cmd == 'status':
            forge_status()
        else:
            print("❌ Unknown command. Try: python forge.py [learn|hackathon|status]")
