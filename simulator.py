import time, random, numpy as np
from datetime import datetime
from database import SessionLocal, EnergyRecord

def run_simulator():
    print("--- Attempting to connect to Database... ---")
    db = SessionLocal()
    print("--- Database Connected! Starting Loop... ---")
    
    try:
        while True:
            print("Generating new reading...") # New debug line
            now = datetime.now()
            val = 50 + 15 * np.sin(now.hour) + random.uniform(-2, 2)
            
            if random.random() < 0.05:
                val = val * 0.2
                print(f"!!! THEFT SIMULATED !!!")

            new_entry = EnergyRecord(timestamp=now, consumption=val, temperature=25.0)
            
            print(f"Saving to DB: {val:.2f} kW at {now.strftime('%H:%M:%S')}") # New debug line
            db.add(new_entry)
            db.commit()
            
            print("Successfully Saved. Waiting 2 seconds...\n")
            time.sleep(2)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}") # This will tell us exactly what's wrong
    finally:
        db.close()
if __name__ == "__main__":
    run_simulator()