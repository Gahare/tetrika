def merge_intervals(times):
    intervals = []
    for i in range(0, len(times), 2):
        intervals.append((times[i], times[i+1]))
    
    intervals.sort(key=lambda x: x[0]) # сортировка по времени подключения

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]: # добавление интервала если объединенный интервал пуст или пересечения нет
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1])) # объединение интервалов изменением конечного времени
        
    merged_times = []
    for interval in merged: # обращение двухмерного массива в одномерный
        merged_times.append(interval[0])
        merged_times.append(interval[1])
    return merged_times


def overlapping_time(pupil, tutor, start, end):
    total_overlap = 0
    pupil_times = merge_intervals(pupil) # исправление несортированных массивов
    tutor_times = merge_intervals(tutor)
    
    i, j = 0, 0
    while i < len(pupil_times) - 1 and j < len(tutor_times) - 1:
        # Ограничение времени подключений в период урока
        on1, off1 = max(pupil_times[i], start), min(pupil_times[i + 1], end)
        on2, off2 = max(tutor_times[j], start), min(tutor_times[j + 1], end)
        # Проверка не пересечение между двумя интервалами
        overlap_start = max(on1, on2)
        overlap_end = min(off1, off2)
        if overlap_start < overlap_end:
            total_overlap += (overlap_end - overlap_start)
        # Сдвиг к следующему интервалу
        if off1 < off2:
            i += 2  # Сдвиг к следующей паре у учеников
        else:
            j += 2  # Сдвиг к следующей паре у учитилей
    return total_overlap

def appearance(intervals: dict[str, list[int]]) -> int:
    start = intervals['lesson'][0]
    end = intervals['lesson'][1]
    pupils = intervals['pupil']
    tutors = intervals['tutor']
    total = overlapping_time(pupils, tutors, start, end)
    return total
              
    
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print('OK')