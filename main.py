

class aA_Helper:

    days_a_week = 7
    application_per_week = 25
    point_goal = 40

    days_past = 4

    current_points = 19.25

    # point values
    onsite = 8
    coding_challenge= 5
    networking_event = 3
    phone_or_video_screen = 2
    practicing_studying_coding = 1
    networking_connection = 5
    submitted_application = .04
    

    def check_week(self):
        pass

    def show_goals(self):
        pass

    def run(self):
        print('aA Job Search Helper\n')
        points_per_day = round((self.point_goal-self.current_points)/(self.days_a_week-self.days_past))
        print(points_per_day)


if __name__ == '__main__':
    app = aA_Helper()
    app.run()
