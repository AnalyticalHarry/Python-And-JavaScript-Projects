function add_time(start_time, duration, starting_day=null) {
    // start time
    let [start, meridiem] = start_time.split(" ");
    let [start_hour, start_minute] = start.split(":").map(Number);
    start_hour %= 12;

    // duration time
    let [duration_hour, duration_minute] = duration.split(":").map(Number);

    // end time
    let end_hour = start_hour + duration_hour;
    let end_minute = start_minute + duration_minute;

    // carry-over of minutes
    if (end_minute >= 60) {
        end_hour += Math.floor(end_minute / 60);
        end_minute %= 60;
    }

    // carry-over of hours
    let carry_days = Math.floor(end_hour / 12);
    end_hour %= 12;

    // meridiem of the end time
    if (carry_days % 2 !== 0) {
        if (meridiem === "AM") {
            meridiem = "PM";
        } else {
            meridiem = "AM";
        }
    }

    // 0 hour to 12 hour
    if (end_hour === 0) {
        end_hour = 12;
    }

    // starting day of the week if provided
    let ending_day = "";
    if (starting_day) {
        starting_day = starting_day.toLowerCase();
        let days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
        let starting_day_index = days.indexOf(starting_day);
        let ending_day_index = (starting_day_index + carry_days) % 7;
        ending_day = days[ending_day_index];
    }

    let end_time = `${String(end_hour).padStart(2, "0")}:${String(end_minute).padStart(2, "0")} ${meridiem}`;
    if (starting_day) {
        if (carry_days === 1) {
            end_time += `, ${ending_day} (next day)`;
        } else if (carry_days > 1) {
            end_time += `, ${ending_day} (${carry_days} days later)`;
        } else {
            end_time += `, ${ending_day}`;
        }
    } else {
        if (carry_days === 1) {
            end_time += " (next day)";
        } else if (carry_days > 1) {
            end_time += ` (${carry_days} days later)`;
        }
    }

    return end_time;
}

console.log(add_time("3:00 PM", "3:10"));
console.log(add_time("11:30 AM", "2:32", "Monday"));
console.log(add_time("11:43 AM", "00:20"));
console.log(add_time("10:10 PM", "3:30"));
console.log(add_time("11:43 PM", "24:20", "tuesday"));
console.log(add_time("6:30 PM", "205:12"));
