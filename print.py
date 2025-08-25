import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

class LoanProcessingDataGenerator:
    def __init__(self):
        # Activity definitions mapping
        self.activity_definitions = {
            'AD-0001': '申込受付',
            'AD-0002': '申込書確認', 
            'AD-0003': '本人確認書類チェック',
            'AD-0004': '収入証明書確認',
            'AD-0005': '勤務先情報確認',
            'AD-0006': '信用情報照会',
            'AD-0007': '初回スコアリング',
            'AD-0008': '詳細審査',
            'AD-0009': '在籍確認',
            'AD-0010': '追加審査',
            'AD-0011': '上席承認',
            'AD-0012': '契約書作成',
            'AD-0013': '最終承認',
            'AD-0014': '融資実行',
            'AD-0015': '完了通知'
        }
        
        # Resources
        self.resources = [f'RES-{str(i).zfill(4)}' for i in range(1, 41)]
        
        # Locations
        self.locations = [
            '新宿支店窓口', '渋谷支店窓口', '池袋支店窓口', '品川支店窓口',
            '上野支店窓口', '大手町支店窓口', '吉祥寺支店窓口', '立川支店窓口',
            '八王子支店窓口', '町田支店窓口', '事務部', '融資部', 'システム', '外部委託'
        ]
        
        # Systems used
        self.systems = [
            '融資システム', 'OCRシステム', '本人確認システム', '勘定系システム',
            '電話', 'ワークフローシステム', '印刷システム'
        ]
        
        # Execution status codes
        self.execution_status = {
            'completed': 100000000,
            'error': 100000001,
            'cancelled': 100000002,
            'timeout': 100000003
        }
        
        # Transition types
        self.transition_types = {
            'normal': 100000000,
            'parallel': 100000001,
            'conditional': 100000002,
            'error': 100000003,
            'escalation': 100000004,
            'rework': 100000005
        }
        
        # Rework reasons
        self.rework_reasons = {
            'normal': 100000000,
            'missing_info': 100000001,
            'verification_failed': 100000002,
            'approval_required': 100000003
        }
        
        # Standard process flow
        self.standard_flow = [
            'AD-0001', 'AD-0002', 'AD-0003', 'AD-0004', 'AD-0005',
            'AD-0006', 'AD-0007', 'AD-0008', 'AD-0009', 'AD-0011',
            'AD-0012', 'AD-0014', 'AD-0015'
        ]
        
    def generate_case_id(self, case_num):
        """Generate case ID"""
        return f'CASE-{str(case_num).zfill(6)}'
    
    def generate_activity_instance_id(self, instance_num):
        """Generate activity instance ID"""
        return f'AI-{str(instance_num).zfill(7)}'
    
    def generate_transition_id(self, transition_num):
        """Generate activity transition ID"""
        return f'AT-{str(transition_num).zfill(7)}'
    
    def generate_loan_amount(self):
        """Generate realistic loan amount in 万円"""
        amounts = [30, 40, 50, 60, 70, 80, 100, 120, 150, 200, 250, 300, 350, 400, 500]
        return random.choice(amounts)
    
    def generate_processing_time(self, activity_def):
        """Generate realistic processing time based on activity type"""
        time_ranges = {
            'AD-0001': (15, 25),  # 申込受付
            'AD-0002': (10, 20),  # 申込書確認
            'AD-0003': (8, 15),   # 本人確認書類チェック
            'AD-0004': (18, 30),  # 収入証明書確認
            'AD-0005': (15, 25),  # 勤務先情報確認
            'AD-0006': (5, 5),    # 信用情報照会
            'AD-0007': (3, 3),    # 初回スコアリング
            'AD-0008': (45, 85),  # 詳細審査
            'AD-0009': (12, 20),  # 在籍確認
            'AD-0010': (40, 60),  # 追加審査
            'AD-0011': (15, 25),  # 上席承認
            'AD-0012': (25, 40),  # 契約書作成
            'AD-0013': (25, 35),  # 最終承認
            'AD-0014': (8, 15),   # 融資実行
            'AD-0015': (5, 5)     # 完了通知
        }
        min_time, max_time = time_ranges.get(activity_def, (10, 30))
        return random.randint(min_time, max_time)
    
    def generate_quality_score(self):
        """Generate quality score (7.0-10.0)"""
        return round(random.uniform(7.5, 9.9), 1)
    
    def calculate_processing_cost(self, processing_minutes, resource):
        """Calculate processing cost based on time and resource"""
        if 'RES-0033' in resource or 'RES-0031' in resource or 'RES-0037' in resource:
            return 0  # System resources have no cost
        cost_per_minute = random.uniform(40, 80)
        return int(processing_minutes * cost_per_minute)
    
    def should_have_rework(self, activity_def):
        """Determine if activity should have rework"""
        rework_probability = {
            'AD-0002': 0.15,  # 申込書確認
            'AD-0004': 0.10,  # 収入証明書確認
            'AD-0009': 0.08,  # 在籍確認
        }
        return random.random() < rework_probability.get(activity_def, 0.02)
    
    def should_have_additional_review(self, loan_amount):
        """Determine if case needs additional review based on loan amount"""
        if loan_amount >= 300:
            return True
        elif loan_amount >= 200:
            return random.random() < 0.7
        elif loan_amount >= 150:
            return random.random() < 0.4
        else:
            return random.random() < 0.1
    
    def should_have_final_approval(self, loan_amount):
        """Determine if case needs final approval based on loan amount"""
        return loan_amount >= 350
    
    def generate_activity_instances(self, start_case_num=31, num_cases=200, start_date='2024-02-05'):
        """Generate activity instance data"""
        instances = []
        instance_counter = 201  # Starting from where original data left off
        
        base_date = pd.to_datetime(start_date)
        
        for case_idx in range(num_cases):
            case_num = start_case_num + case_idx
            case_id = self.generate_case_id(case_num)
            
            # Generate loan amount for this case
            loan_amount = self.generate_loan_amount()
            
            # Determine if case needs additional review and final approval
            needs_additional = self.should_have_additional_review(loan_amount)
            needs_final = self.should_have_final_approval(loan_amount)
            
            # Build process flow for this case
            process_flow = self.standard_flow.copy()
            if needs_additional:
                process_flow.insert(process_flow.index('AD-0009') + 1, 'AD-0010')
            if needs_final:
                process_flow.insert(process_flow.index('AD-0011') + 1, 'AD-0013')
            
            # Random start time for the case
            case_start = base_date + timedelta(
                days=random.randint(0, 60),
                hours=random.randint(8, 16),
                minutes=random.randint(0, 59)
            )
            
            current_time = case_start
            execution_seq = 1
            
            for activity_def in process_flow:
                activity_name = self.activity_definitions[activity_def]
                
                # Check for rework
                iteration = 1
                should_rework = self.should_have_rework(activity_def)
                
                # First iteration (potentially with error)
                if should_rework:
                    # First attempt with error
                    processing_minutes = self.generate_processing_time(activity_def)
                    waiting_minutes = random.randint(0, 20)
                    queue_minutes = random.randint(0, 15)
                    
                    resource = random.choice(self.resources[:30])
                    location = self.determine_location(activity_def)
                    system = self.determine_system(activity_def)
                    
                    instance = {
                        'activityinstanceid': self.generate_activity_instance_id(instance_counter),
                        'name': f'{case_id} - {activity_name} ({iteration})',
                        'processcase': case_id,
                        'activitydefinition': activity_def,
                        'resource': resource,
                        'executionsequence': execution_seq,
                        'iterationnumber': iteration,
                        'startedat': current_time.strftime('%Y-%m-%d %H:%M:%S'),
                        'completedat': (current_time + timedelta(minutes=processing_minutes)).strftime('%Y-%m-%d %H:%M:%S'),
                        'processingminutes': processing_minutes,
                        'waitingminutes': waiting_minutes,
                        'queueminutes': queue_minutes,
                        'executionstatus': self.execution_status['error'],
                        'reworkreason': self.rework_reasons['missing_info'],
                        'processingcost': self.calculate_processing_cost(processing_minutes, resource),
                        'qualityscore': round(random.uniform(6.5, 7.5), 1),  # Lower score for error
                        'location': location,
                        'systemused': system,
                        'comments': self.generate_comment(activity_def, loan_amount, True),
                        'isrework': 'FALSE',
                        'slabreached': random.choice(['TRUE', 'FALSE'])
                    }
                    instances.append(instance)
                    instance_counter += 1
                    execution_seq += 1
                    
                    # Move time forward
                    current_time += timedelta(minutes=processing_minutes + random.randint(30, 120))
                    iteration = 2
                
                # Successful iteration
                processing_minutes = self.generate_processing_time(activity_def)
                waiting_minutes = random.randint(0, 20) if iteration == 1 else random.randint(20, 60)
                queue_minutes = random.randint(0, 15)
                
                resource = random.choice(self.resources[:30])
                location = self.determine_location(activity_def)
                system = self.determine_system(activity_def)
                
                instance = {
                    'activityinstanceid': self.generate_activity_instance_id(instance_counter),
                    'name': f'{case_id} - {activity_name} ({iteration})',
                    'processcase': case_id,
                    'activitydefinition': activity_def,
                    'resource': resource,
                    'executionsequence': execution_seq,
                    'iterationnumber': iteration,
                    'startedat': current_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'completedat': (current_time + timedelta(minutes=processing_minutes)).strftime('%Y-%m-%d %H:%M:%S'),
                    'processingminutes': processing_minutes,
                    'waitingminutes': waiting_minutes,
                    'queueminutes': queue_minutes,
                    'executionstatus': self.execution_status['completed'],
                    'reworkreason': '' if iteration == 1 else self.rework_reasons['normal'],
                    'processingcost': self.calculate_processing_cost(processing_minutes, resource),
                    'qualityscore': self.generate_quality_score(),
                    'location': location,
                    'systemused': system,
                    'comments': self.generate_comment(activity_def, loan_amount, False),
                    'isrework': 'TRUE' if iteration > 1 else 'FALSE',
                    'slabreached': self.determine_sla_breach(activity_def, loan_amount)
                }
                instances.append(instance)
                instance_counter += 1
                execution_seq += 1
                
                # Move time forward
                current_time += timedelta(minutes=processing_minutes + random.randint(5, 30))
                
                # Add potential overnight/weekend delays
                if current_time.hour >= 18:
                    current_time = current_time.replace(hour=9, minute=0) + timedelta(days=1)
                if current_time.weekday() >= 5:  # Weekend
                    days_to_monday = 7 - current_time.weekday()
                    current_time += timedelta(days=days_to_monday)
        
        return pd.DataFrame(instances)
    
    def determine_location(self, activity_def):
        """Determine location based on activity type"""
        if activity_def == 'AD-0001':
            return random.choice(self.locations[:10])  # Branch offices
        elif activity_def in ['AD-0002', 'AD-0003', 'AD-0004', 'AD-0005']:
            return '事務部'
        elif activity_def in ['AD-0008', 'AD-0009', 'AD-0010', 'AD-0011', 'AD-0013']:
            return '融資部'
        elif activity_def in ['AD-0006', 'AD-0007', 'AD-0014', 'AD-0015']:
            return 'システム'
        elif activity_def == 'AD-0012':
            return '外部委託'
        else:
            return random.choice(self.locations[10:])
    
    def determine_system(self, activity_def):
        """Determine system used based on activity type"""
        system_mapping = {
            'AD-0001': '融資システム',
            'AD-0002': 'OCRシステム',
            'AD-0003': '本人確認システム',
            'AD-0004': 'OCRシステム',
            'AD-0005': '勘定系システム',
            'AD-0006': '融資システム',
            'AD-0007': '融資システム',
            'AD-0008': '融資システム',
            'AD-0009': '電話',
            'AD-0010': '融資システム',
            'AD-0011': 'ワークフローシステム',
            'AD-0012': '印刷システム',
            'AD-0013': 'ワークフローシステム',
            'AD-0014': '勘定系システム',
            'AD-0015': 'ワークフローシステム'
        }
        return system_mapping.get(activity_def, '融資システム')
    
    def generate_comment(self, activity_def, loan_amount, is_error=False):
        """Generate realistic comment based on activity and context"""
        if is_error:
            error_comments = [
                '記入漏れありエラー',
                '書類不備あり',
                '追加情報必要',
                '確認事項あり',
                '再提出要請'
            ]
            return random.choice(error_comments)
        
        comments = {
            'AD-0001': f'{loan_amount}万円申込受付',
            'AD-0002': '記入内容確認完了',
            'AD-0003': '本人確認完了',
            'AD-0004': '収入証明確認完了',
            'AD-0005': '勤務先確認完了',
            'AD-0006': '信用情報照会完了',
            'AD-0007': f'スコア{random.randint(60, 90)}点',
            'AD-0008': f'{loan_amount}万円審査完了',
            'AD-0009': '在籍確認完了',
            'AD-0010': '追加審査完了',
            'AD-0011': '承認完了',
            'AD-0012': '契約書作成完了',
            'AD-0013': '最終承認完了',
            'AD-0014': '振込実行完了',
            'AD-0015': '通知送信完了'
        }
        return comments.get(activity_def, '処理完了')
    
    def determine_sla_breach(self, activity_def, loan_amount):
        """Determine if SLA was breached"""
        # Higher amounts have higher chance of SLA breach
        breach_probability = 0.05
        if loan_amount >= 300:
            breach_probability = 0.15
        elif loan_amount >= 200:
            breach_probability = 0.10
        
        # Certain activities more prone to SLA breach
        if activity_def in ['AD-0008', 'AD-0010']:
            breach_probability *= 1.5
        
        return 'TRUE' if random.random() < breach_probability else 'FALSE'
    
    def generate_transitions(self, activity_instances_df):
        """Generate transition data based on activity instances"""
        transitions = []
        transition_counter = 180  # Starting from where original data left off
        
        # Group by case
        for case_id in activity_instances_df['processcase'].unique():
            case_activities = activity_instances_df[
                activity_instances_df['processcase'] == case_id
            ].sort_values('executionsequence')
            
            # Generate transitions between consecutive activities
            for i in range(len(case_activities) - 1):
                from_activity = case_activities.iloc[i]
                to_activity = case_activities.iloc[i + 1]
                
                # Determine transition type
                if from_activity['iterationnumber'] < to_activity['iterationnumber']:
                    trans_type = self.transition_types['rework']
                    trans_reason = 'リワーク処理'
                elif from_activity['activitydefinition'] in ['AD-0003', 'AD-0004'] and \
                     to_activity['activitydefinition'] in ['AD-0004', 'AD-0005']:
                    trans_type = self.transition_types['parallel']
                    trans_reason = '並行処理開始'
                else:
                    trans_type = self.transition_types['normal']
                    trans_reason = self.generate_transition_reason(
                        from_activity['activitydefinition'],
                        to_activity['activitydefinition']
                    )
                
                # Calculate handoff duration
                from_complete = pd.to_datetime(from_activity['completedat'])
                to_start = pd.to_datetime(to_activity['startedat'])
                handoff_minutes = int((to_start - from_complete).total_seconds() / 60)
                
                # Determine if bottleneck
                is_bottleneck = 'TRUE' if handoff_minutes > 60 else 'FALSE'
                
                transition = {
                    'activitytransitionid': self.generate_transition_id(transition_counter),
                    'name': f"{case_id}: {from_activity['name'].split(' - ')[1]}→{to_activity['name'].split(' - ')[1]}",
                    'processcase': case_id,
                    'fromactivity': from_activity['activityinstanceid'],
                    'toactivity': to_activity['activityinstanceid'],
                    'transitiontype': trans_type,
                    'transitiontime': to_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'handoffduration': max(0, handoff_minutes),
                    'waitingduration': to_activity['waitingminutes'],
                    'fromresource': from_activity['resource'],
                    'toresource': to_activity['resource'],
                    'transitionreason': trans_reason,
                    'isbottleneck': is_bottleneck
                }
                transitions.append(transition)
                transition_counter += 1
        
        return pd.DataFrame(transitions)
    
    def generate_transition_reason(self, from_def, to_def):
        """Generate transition reason based on activity types"""
        reasons = {
            ('AD-0001', 'AD-0002'): '営業店から事務部へ',
            ('AD-0002', 'AD-0003'): '事務部内連携',
            ('AD-0003', 'AD-0004'): '並行処理開始',
            ('AD-0004', 'AD-0005'): '事務部内連携',
            ('AD-0005', 'AD-0006'): '事務部からシステムへ',
            ('AD-0006', 'AD-0007'): 'システム内連携',
            ('AD-0007', 'AD-0008'): 'システムから融資部へ',
            ('AD-0008', 'AD-0009'): '融資部内連携',
            ('AD-0009', 'AD-0010'): '追加審査必要',
            ('AD-0009', 'AD-0011'): '審査から承認へ',
            ('AD-0010', 'AD-0011'): '追加審査から承認へ',
            ('AD-0011', 'AD-0012'): '融資部から外部委託へ',
            ('AD-0011', 'AD-0013'): '高額案件で最終承認必要',
            ('AD-0013', 'AD-0012'): '最終承認から契約書作成へ',
            ('AD-0012', 'AD-0014'): '外部委託からシステムへ',
            ('AD-0014', 'AD-0015'): 'システム内連携'
        }
        return reasons.get((from_def, to_def), '標準フロー')

# Generate the data
generator = LoanProcessingDataGenerator()

# Generate 500 new cases starting from case 31
print("Generating activity instances...")
activity_instances = generator.generate_activity_instances(
    start_case_num=31,
    num_cases=500,
    start_date='2024-02-06'
)

print(f"Generated {len(activity_instances)} activity instances")

# Generate transitions based on the activity instances
print("Generating activity transitions...")
activity_transitions = generator.generate_transitions(activity_instances)

print(f"Generated {len(activity_transitions)} activity transitions")

# Save to CSV files
activity_instances.to_csv('activity_instance_expanded_additional.csv', index=False, encoding='utf-8-sig')
activity_transitions.to_csv('activity_transition_expanded_additional.csv', index=False, encoding='utf-8-sig')

print("\nData generation complete!")
print(f"Activity instances saved to: activity_instance_expanded_additional.csv")
print(f"Activity transitions saved to: activity_transition_expanded_additional.csv")

# Display sample data
print("\nSample Activity Instances:")
print(activity_instances.head())
print("\nSample Activity Transitions:")
print(activity_transitions.head())

# Display summary statistics
print("\nSummary Statistics:")
print(f"Total cases: {activity_instances['processcase'].nunique()}")
print(f"Total activity instances: {len(activity_instances)}")
print(f"Total transitions: {len(activity_transitions)}")
print(f"Rework instances: {(activity_instances['isrework'] == 'TRUE').sum()}")
print(f"SLA breaches: {(activity_instances['slabreached'] == 'TRUE').sum()}")
print(f"Bottleneck transitions: {(activity_transitions['isbottleneck'] == 'TRUE').sum()}")
