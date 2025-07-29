from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student

class Command(BaseCommand):
    help = 'Populate database with sample student data'

    def handle(self, *args, **options):
        # Create superuser if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser "admin" created with password "admin123"')
            )

        # Sample student data
        student_data = [
            {'name': 'Aayush Sharma', 'student_id': '001', 'department': 'Computer Science'},
            {'name': 'Priya Patel', 'student_id': '002', 'department': 'Information Technology'},
            {'name': 'Rajesh Kumar', 'student_id': '003', 'department': 'Software Engineering'},
            {'name': 'Sneha Gupta', 'student_id': '004', 'department': 'Electronics'},
            {'name': 'Vikash Singh', 'student_id': '005', 'department': 'Mechanical Engineering'},
            {'name': 'Anita Thapa', 'student_id': '006', 'department': 'Civil Engineering'},
            {'name': 'Suresh Yadav', 'student_id': '007', 'department': 'Computer Science'},
            {'name': 'Kavya Joshi', 'student_id': '008', 'department': 'Information Technology'},
            {'name': 'Rohit Pandey', 'student_id': '009', 'department': 'Software Engineering'},
            {'name': 'Meera Shah', 'student_id': '010', 'department': 'Electronics'},
            {'name': 'Arjun Khadka', 'student_id': '011', 'department': 'Computer Science'},
            {'name': 'Pooja Agarwal', 'student_id': '012', 'department': 'Information Technology'},
            {'name': 'Nischal Rai', 'student_id': '013', 'department': 'Software Engineering'},
            {'name': 'Ritu Kumari', 'student_id': '014', 'department': 'Electronics'},
            {'name': 'Sandip Ghimire', 'student_id': '015', 'department': 'Mechanical Engineering'},
            {'name': 'Shikha Bansal', 'student_id': '016', 'department': 'Civil Engineering'},
            {'name': 'Manish Tamang', 'student_id': '017', 'department': 'Computer Science'},
            {'name': 'Deepika Rana', 'student_id': '018', 'department': 'Information Technology'},
            {'name': 'Bibek Gurung', 'student_id': '019', 'department': 'Software Engineering'},
            {'name': 'Shristi Bista', 'student_id': '020', 'department': 'Electronics'},
            {'name': 'Nabin Shrestha', 'student_id': '021', 'department': 'Computer Science'},
            {'name': 'Sunita Karki', 'student_id': '022', 'department': 'Information Technology'},
            {'name': 'Dipesh Magar', 'student_id': '023', 'department': 'Software Engineering'},
            {'name': 'Aarti Chaudhary', 'student_id': '024', 'department': 'Electronics'},
            {'name': 'Ramesh Bhatta', 'student_id': '025', 'department': 'Mechanical Engineering'},
            {'name': 'Sita Devi', 'student_id': '026', 'department': 'Civil Engineering'},
            {'name': 'Kamal Adhikari', 'student_id': '027', 'department': 'Computer Science'},
            {'name': 'Binita Poudel', 'student_id': '028', 'department': 'Information Technology'},
            {'name': 'Pramod Limbu', 'student_id': '029', 'department': 'Software Engineering'},
            {'name': 'Nisha Maharjan', 'student_id': '030', 'department': 'Electronics'},
            {'name': 'Sagar Basnet', 'student_id': '031', 'department': 'Computer Science'},
            {'name': 'Rashmi Koju', 'student_id': '032', 'department': 'Information Technology'},
            {'name': 'Umesh Dhakal', 'student_id': '033', 'department': 'Software Engineering'},
            {'name': 'Sabina Parajuli', 'student_id': '034', 'department': 'Electronics'},
            {'name': 'Kiran Regmi', 'student_id': '035', 'department': 'Mechanical Engineering'},
            {'name': 'Urmila Khatri', 'student_id': '036', 'department': 'Civil Engineering'},
            {'name': 'Hem Raj Oli', 'student_id': '037', 'department': 'Computer Science'},
            {'name': 'Sushma Neupane', 'student_id': '038', 'department': 'Information Technology'},
            {'name': 'Ashok Dahal', 'student_id': '039', 'department': 'Software Engineering'},
            {'name': 'Kamala Subedi', 'student_id': '040', 'department': 'Electronics'},
            {'name': 'Jeevan Bhattarai', 'student_id': '041', 'department': 'Computer Science'},
            {'name': 'Gita Pandey', 'student_id': '042', 'department': 'Information Technology'},
            {'name': 'Krishna Lamsal', 'student_id': '043', 'department': 'Software Engineering'},
            {'name': 'Radha Tiwari', 'student_id': '044', 'department': 'Electronics'},
            {'name': 'Mohan KC', 'student_id': '045', 'department': 'Mechanical Engineering'},
            {'name': 'Sarita Thapa', 'student_id': '046', 'department': 'Civil Engineering'},
            {'name': 'Lok Bahadur', 'student_id': '047', 'department': 'Computer Science'},
            {'name': 'Purnima Rana', 'student_id': '048', 'department': 'Information Technology'},
            {'name': 'Bishnu Silwal', 'student_id': '049', 'department': 'Software Engineering'},
            {'name': 'Indira Joshi', 'student_id': '050', 'department': 'Electronics'},
        ]

        # Create students if they don't exist
        created_count = 0
        for data in student_data:
            student, created = Student.objects.get_or_create(
                student_id=data['student_id'],
                defaults={
                    'name': data['name'],
                    'department': data['department']
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} students')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total students in database: {Student.objects.count()}')
        )
