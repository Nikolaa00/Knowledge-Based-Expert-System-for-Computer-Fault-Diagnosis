# Фаза 03 — База на знаење

Копирај го целиот овој фајл во нов агентски разговор. Оваа фаза го полни знаењето. Не ја имплементира машината и не го менува екранот.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01 и 02 веќе ги имаат правилата, skill-от и скелетот. Прочитај ги `.cursor/rules/architecture.mdc` и `src/pc_fault_diagnosis/knowledge/repository.py` пред измена. Репозиториумот веќе го валидира обликот. Не го олабавувај за да помине базата.

## Што веќе постои

Празен `knowledge/computer_faults.yaml` и репозиториум што ја вчитува базата на потсистеми, симптоми, дефекти, факти и правила. `ForwardChainingEngine.infer` сè уште фрла `NotImplementedError`. Така и останува.

## Што да направиш

Замени го празниот YAML со каталогот подолу. Зачувај ги идентификаторите, врските и македонските текстови. Текстот е дел од знаењето: краток, конкретен, како што би го кажал техничар. Не додавај симптоми, дефекти или правила што ги нема овде. Секој симптом влегува во барем едно правило, и тоа веќе е исполнето со овој каталог.

Фајлот останува UTF-8. По полнењето, вчитај го преку `YamlKnowledgeRepository` и поправи ја валидацијата само ако каталогот открие вистинска грешка во репозиториумот. Не менувај го договорот за полињата.

### Каталог

```yaml
subsystems:
  - id: power
    label_mk: Напојување
  - id: boot
    label_mk: Бутање
  - id: display
    label_mk: Екран
  - id: storage
    label_mk: Диск
  - id: memory
    label_mk: Меморија
  - id: network
    label_mk: Мрежа
  - id: performance
    label_mk: Перформанси
  - id: peripherals
    label_mk: Периферни уреди

symptoms:
  - id: no_power_led
    subsystem: power
    label_mk: Не свети индикаторот за напојување
    description_mk: Куќиштето не дава знак дека добива струја.
  - id: no_fans
    subsystem: power
    label_mk: Вентилаторите не се вртат
    description_mk: По притискање на копчето нема вртење ниту шум од вентилатор.
  - id: burning_smell
    subsystem: power
    label_mk: Мирис на изгорено
    description_mk: Од куќиштето се чувствува мирис на изгорена електроника.
  - id: psu_clicks
    subsystem: power
    label_mk: Напојувањето кликнува и се гаси
    description_mk: Се слуша клик, уредот за миг фаќа струја и пак се гаси.
  - id: works_after_reseating_cable
    subsystem: power
    label_mk: Работи откако ќе се помрдне кабелот
    description_mk: Се вклучува само кога кабелот за струја ќе се притисне повторно.
  - id: no_post
    subsystem: boot
    label_mk: Нема POST
    description_mk: Нема обичен екран за проверка и системот не продолжува кон бутање.
  - id: beeps_continuous
    subsystem: boot
    label_mk: Континуирани звучни сигнали
    description_mk: Звучникот на плочата писка без прекин.
  - id: beeps_one_long
    subsystem: boot
    label_mk: Еден долг звучен сигнал
    description_mk: Се слуша еден долг сигнал при вклучување.
  - id: restarts_before_os
    subsystem: boot
    label_mk: Се рестартира пред системот
    description_mk: Уредот се гаси и пали повторно пред да се појави оперативниот систем.
  - id: bios_resets
    subsystem: boot
    label_mk: BIOS поставките се ресетираат
    description_mk: Датумот и поставките се губат по исклучување од струја.
  - id: no_signal
    subsystem: display
    label_mk: Мониторот јавува нема сигнал
    description_mk: Мониторот е вклучен, но јавува дека нема видеосигнал.
  - id: artifacts
    subsystem: display
    label_mk: Линии или коцки на сликата
    description_mk: На екранот има погрешни бои, линии или коцки.
  - id: backlight_only
    subsystem: display
    label_mk: Екранот е црн, светлото работи
    description_mk: Панелот свети слабо, но нема слика.
  - id: external_display_ok
    subsystem: display
    label_mk: Надворешниот монитор е исправен
    description_mk: Истата слика е добра на друг монитор или телевизор.
  - id: slow_boot_disk
    subsystem: storage
    label_mk: Долго бутање со активен диск
    description_mk: Логото стои долго, а дискот постојано работи.
  - id: clicking_disk
    subsystem: storage
    label_mk: Чукање од дискот
    description_mk: Се слуша ритмичко чукање или стругање од дискот.
  - id: files_disappear
    subsystem: storage
    label_mk: Датотеки не се отвораат
    description_mk: Датотеки исчезнуваат, се оштетуваат или не се отвораат.
  - id: smart_warning
    subsystem: storage
    label_mk: Предупредување за дискот
    description_mk: Системот јавува дека дискот може да откаже.
  - id: random_freeze
    subsystem: memory
    label_mk: Случајно замрзнување
    description_mk: Сликата застанува без порака и помага само рестарт.
  - id: bsod_memory
    subsystem: memory
    label_mk: Син екран поврзан со меморија
    description_mk: Синиот екран споменува меморија или memory management.
  - id: passes_one_stick
    subsystem: memory
    label_mk: Работи со една мемориска плочка
    description_mk: Со едната плочка бута, со двете не бута.
  - id: memtest_errors
    subsystem: memory
    label_mk: MemTest јавува грешки
    description_mk: Тестот на меморијата пријавува грешки.
  - id: no_wifi
    subsystem: network
    label_mk: Нема Wi-Fi мрежи
    description_mk: Адаптерот не прикажува ниту една безжична мрежа.
  - id: wifi_drops
    subsystem: network
    label_mk: Wi-Fi врската се кине
    description_mk: Врската се воспоставува и пак исчезнува по кратко време.
  - id: ethernet_dead
    subsystem: network
    label_mk: Кабелската мрежа не добива адреса
    description_mk: Приклучен кабел не добива мрежна адреса.
  - id: other_devices_online
    subsystem: network
    label_mk: Другите уреди се на мрежа
    description_mk: Телефон или друг компјутер на истата мрежа работи нормално.
  - id: high_cpu_idle
    subsystem: performance
    label_mk: Висок процесор во мирување
    description_mk: Процесорот е зафатен иако не е отворена тешка програма.
  - id: thermal_shutdown
    subsystem: performance
    label_mk: Се гаси под оптоварување
    description_mk: Уредот се исклучува кога ќе се загрее при работа.
  - id: loud_fans_hot
    subsystem: performance
    label_mk: Гласни вентилатори и топол воздух
    description_mk: Вентилаторите вијат, а воздухот од куќиштето е топол.
  - id: stutter_games
    subsystem: performance
    label_mk: Сецкање во игри и 3D
    description_mk: Сецкањето се јавува во игри или други тродимензионални програми.
  - id: usb_not_detected
    subsystem: peripherals
    label_mk: USB уредот не се препознава
    description_mk: Уредот е приклучен, но не се појавува во системот.
  - id: usb_power_only
    subsystem: peripherals
    label_mk: USB уредот само добива струја
    description_mk: Свети лампичката на уредот, но компјутерот не го гледа.
  - id: keyboard_repeat
    subsystem: peripherals
    label_mk: Тастатурата повторува или молчи
    description_mk: Знаците се повторуваат, или дел од типките не реагираат.
  - id: works_on_other_port
    subsystem: peripherals
    label_mk: Работи на друга порта
    description_mk: Истиот уред работи кога ќе се префрли на друга порта.

facts:
  - id: power_path_dead
    label_mk: Плочата не добива струја
  - id: memory_subsystem_suspect
    label_mk: Сомнителен мемориски потсистем

faults:
  - id: faulty_psu
    name_mk: Неисправно напојување
    summary_mk: Напојувањето не испорачува стабилна струја до плочата.
  - id: loose_power_cable
    name_mk: Лабав кабел за напојување
    summary_mk: Струјата се губи на кабелот или на приклучокот.
  - id: burnt_component
    name_mk: Изгорена компонента
    summary_mk: Има знак за изгорена компонента во патеката на напојување.
  - id: loose_ram
    name_mk: Лошо наместена меморија
    summary_mk: Мемориската плочка не прави сигурен контакт.
  - id: faulty_ram
    name_mk: Неисправна меморија
    summary_mk: Меморијата враќа грешки или го запира бутањето.
  - id: dead_cmos_battery
    name_mk: Испразнета CMOS батерија
    summary_mk: Батеријата на плочата не ги чува поставките.
  - id: faulty_gpu
    name_mk: Неисправна графичка картичка
    summary_mk: Графичката картичка дава погрешна или никаква слика.
  - id: faulty_display_panel
    name_mk: Неисправен екран
    summary_mk: Панелот на екранот не ја прикажува сликата што уредот ја испраќа.
  - id: failing_disk
    name_mk: Диск што откажува
    summary_mk: Дискот има механички или SMART знак дека откажува.
  - id: corrupted_filesystem
    name_mk: Оштетен датотечен систем
    summary_mk: Податоците се оштетени без знак дека дискот механички откажува.
  - id: faulty_wifi_adapter
    name_mk: Неисправен безжичен адаптер
    summary_mk: Безжичниот адаптер не држи врска, а мрежата инаку работи.
  - id: bad_ethernet_cable_or_port
    name_mk: Лош кабел или мрежна порта
    summary_mk: Кабелската врска не добива адреса иако мрежата работи за другите.
  - id: overheating
    name_mk: Прегревање
    summary_mk: Уредот се гаси затоа што не се лади доволно.
  - id: background_cpu_load
    name_mk: Позадинско оптоварување
    summary_mk: Процесорот го троши процес што работи во позадина.
  - id: faulty_usb_port
    name_mk: Неисправна USB порта
    summary_mk: Портата дава струја или контакт, но не ја држи врската стабилно.
  - id: faulty_keyboard
    name_mk: Неисправна тастатура
    summary_mk: Тастатурата повторува знаци или не реагира на сите типки.

rules:
  - id: rule_power_path_dead
    when_present: [no_power_led, no_fans]
    when_absent: [burning_smell]
    conclude: {kind: fact, id: power_path_dead}
    explanation_mk: Нема светло и нема вртење на вентилаторите, без мирис на изгорено. Плочата не добива струја.
    recommendations_mk: []
  - id: rule_faulty_psu
    when_present: [power_path_dead, psu_clicks]
    when_absent: [works_after_reseating_cable]
    conclude: {kind: fault, id: faulty_psu}
    explanation_mk: Патеката на струја е мртва, а напојувањето кликнува и се гаси. Тоа е знак за неисправно напојување.
    recommendations_mk:
      - Исклучи го кабелот и провери дали има мирис на изгорено пред повторно вклучување.
      - Испитај со друго познато исправно напојување.
  - id: rule_loose_cable
    when_present: [power_path_dead, works_after_reseating_cable]
    when_absent: [psu_clicks]
    conclude: {kind: fault, id: loose_power_cable}
    explanation_mk: Струјата се појавува дури откако кабелот ќе се помрдне. Контактот на кабелот е лабав.
    recommendations_mk:
      - Замени го кабелот за напојување.
      - Провери ја утичницата и продолжниот кабел со друг уред.
  - id: rule_burnt_component
    when_present: [burning_smell]
    when_absent: [works_after_reseating_cable]
    conclude: {kind: fault, id: burnt_component}
    explanation_mk: Се чувствува мирис на изгорено. Не вклучувај го уредот повторно.
    recommendations_mk:
      - Остави го уредот исклучен од струја.
      - Отвори го само ако знаеш што бараш, или однеси го на преглед.
  - id: rule_boot_loop_psu
    when_present: [restarts_before_os, psu_clicks]
    when_absent: [burning_smell, no_power_led, no_fans]
    conclude: {kind: fault, id: faulty_psu}
    explanation_mk: Уредот се рестартира пред системот, а напојувањето кликнува. Напојувањето не ја држи струјата.
    recommendations_mk:
      - Исклучи ги непотребните USB уреди и пробај уште еднаш.
      - Ако кликот остане, замени го напојувањето.
  - id: rule_memory_suspect
    when_present: [no_post, beeps_continuous]
    when_absent: []
    conclude: {kind: fact, id: memory_subsystem_suspect}
    explanation_mk: Нема POST, а звучникот писка без прекин. Плочата укажува на меморија.
    recommendations_mk: []
  - id: rule_memory_suspect_long_beep
    when_present: [no_post, beeps_one_long]
    when_absent: []
    conclude: {kind: fact, id: memory_subsystem_suspect}
    explanation_mk: Нема POST и се слуша еден долг сигнал. Проверката застанува на меморијата.
    recommendations_mk: []
  - id: rule_loose_ram
    when_present: [memory_subsystem_suspect, passes_one_stick]
    when_absent: [memtest_errors]
    conclude: {kind: fault, id: loose_ram}
    explanation_mk: Со една плочка бута, а тестот не јавува грешка. Контактот на плочката е поверојатен од изгорена меморија.
    recommendations_mk:
      - Извади ги плочките, исчисти го контактот и намести ги повторно.
      - Пробај ја секоја плочка во првиот слот.
  - id: rule_faulty_ram
    when_present: [memory_subsystem_suspect, memtest_errors]
    when_absent: []
    conclude: {kind: fault, id: faulty_ram}
    explanation_mk: Знакот при бутање води до меморија, а MemTest потврдува грешки.
    recommendations_mk:
      - Тестирај ја секоја плочка одделно.
      - Замени ја плочката што јавува грешка.
  - id: rule_faulty_ram_bsod
    when_present: [bsod_memory, random_freeze]
    when_absent: [thermal_shutdown]
    conclude: {kind: fault, id: faulty_ram}
    explanation_mk: Син екран за меморија и замрзнување, без гасење од топлина. Меморијата е неисправна.
    recommendations_mk:
      - Пушти MemTest од USB.
      - Ако грешката се повторува на една плочка, замени ја.
  - id: rule_cmos_battery
    when_present: [bios_resets]
    when_absent: [no_power_led]
    conclude: {kind: fault, id: dead_cmos_battery}
    explanation_mk: Поставките се губат иако уредот инаку добива струја. CMOS батеријата не држи.
    recommendations_mk:
      - Замени ја CR2032 батеријата на плочата.
      - По замена постави датум и провери дали се задржува.
  - id: rule_faulty_gpu
    when_present: [artifacts, stutter_games]
    when_absent: [external_display_ok]
    conclude: {kind: fault, id: faulty_gpu}
    explanation_mk: Има артефакти и сецкање во 3D, а сликата не е добра ни на друг екран.
    recommendations_mk:
      - Извади ја картичката и намести ја повторно.
      - Пробај со друга картичка или со вградената графика.
  - id: rule_no_signal_gpu
    when_present: [no_signal, no_post]
    when_absent: [no_power_led]
    conclude: {kind: fault, id: faulty_gpu}
    explanation_mk: Струја има, но нема POST ниту видеосигнал. Графичкиот излез не тргнува.
    recommendations_mk:
      - Провери дали кабелот е во картичката, не во плочата.
      - Отстрани ја дискретната картичка и пробај со вградената графика.
  - id: rule_display_panel
    when_present: [backlight_only, external_display_ok]
    when_absent: []
    conclude: {kind: fault, id: faulty_display_panel}
    explanation_mk: Надворешниот екран е добар, а вградениот панел останува црн. Панелот или неговиот кабел е неисправен.
    recommendations_mk:
      - Провери го кабелот на панелот ако уредот се отвора лесно.
      - Користи надворешен монитор до замена на панелот.
  - id: rule_failing_disk
    when_present: [clicking_disk, slow_boot_disk]
    when_absent: []
    conclude: {kind: fault, id: failing_disk}
    explanation_mk: Дискот чука и бутањето е долго. Тоа е механички знак дека дискот откажува.
    recommendations_mk:
      - Не инсталирај систем одново пред да ги ископираш важните податоци.
      - Замени го дискот и провери го стариот од друг компјутер само за копирање.
  - id: rule_smart_disk
    when_present: [smart_warning, slow_boot_disk]
    when_absent: []
    conclude: {kind: fault, id: failing_disk}
    explanation_mk: Системот предупредува за дискот, а бутањето е бавно. Дискот откажува.
    recommendations_mk:
      - Ископирај ги податоците веднаш.
      - Замени го дискот; не го игнорирај предупредувањето.
  - id: rule_corrupted_filesystem
    when_present: [files_disappear, slow_boot_disk]
    when_absent: [clicking_disk]
    conclude: {kind: fault, id: corrupted_filesystem}
    explanation_mk: Датотеките не се отвораат и бутањето е бавно, без чукање. Датотечниот систем е оштетен.
    recommendations_mk:
      - Пушти проверка на дискот од системот.
      - Прекини го запишувањето додека не се ископира она што сè уште се отвора.
  - id: rule_wifi_adapter
    when_present: [no_wifi, other_devices_online]
    when_absent: [ethernet_dead]
    conclude: {kind: fault, id: faulty_wifi_adapter}
    explanation_mk: Другите уреди ја гледаат мрежата, а овој не прикажува ниту една Wi-Fi мрежа.
    recommendations_mk:
      - Вклучи го адаптерот со функциското копче или од поставките.
      - Ако и по драјвер не гледа мрежа, адаптерот е неисправен.
  - id: rule_wifi_drops
    when_present: [wifi_drops, other_devices_online]
    when_absent: []
    conclude: {kind: fault, id: faulty_wifi_adapter}
    explanation_mk: Врската се кине само на овој уред. Безжичниот адаптер не ја држи мрежата.
    recommendations_mk:
      - Заборави ја мрежата и поврзи се повторно.
      - Пробај USB адаптер за да видиш дали вградениот откажува.
  - id: rule_ethernet
    when_present: [ethernet_dead, other_devices_online]
    when_absent: [no_wifi]
    conclude: {kind: fault, id: bad_ethernet_cable_or_port}
    explanation_mk: Кабелот не добива адреса, а другите уреди се на мрежа. Кабелот или портата не ја носат врската.
    recommendations_mk:
      - Пробај друг кабел и друга порта на рутерот.
      - Ако друг кабел работи, замени го кабелот; ако не работи, портата на компјутерот е сомнителна.
  - id: rule_overheating
    when_present: [thermal_shutdown, loud_fans_hot]
    when_absent: [no_fans]
    conclude: {kind: fault, id: overheating}
    explanation_mk: Вентилаторите работат гласно, воздухот е топол и уредот се гаси под товар.
    recommendations_mk:
      - Исчисти ја прашината и провери дали вентилаторот навистина се врти.
      - Провери ја пастата и дали уредот има воздух околу отворите.
  - id: rule_background_cpu
    when_present: [high_cpu_idle]
    when_absent: [thermal_shutdown]
    conclude: {kind: fault, id: background_cpu_load}
    explanation_mk: Процесорот е зафатен во мирување, без гасење од топлина. Товарот доаѓа од позадински процес.
    recommendations_mk:
      - Отвори го управувачот на задачи и подреди по процесор.
      - Запри го процесот што троши и провери дали се враќа по рестарт.
  - id: rule_usb_port
    when_present: [usb_not_detected, works_on_other_port]
    when_absent: []
    conclude: {kind: fault, id: faulty_usb_port}
    explanation_mk: Уредот се гледа на друга порта, значи уредот е исправен, а оваа порта не е.
    recommendations_mk:
      - Користи ја портата што работи.
      - Ако повеќе порти на иста група не работат, провери го кабелот на предниот панел.
  - id: rule_usb_power_only
    when_present: [usb_power_only, usb_not_detected]
    when_absent: []
    conclude: {kind: fault, id: faulty_usb_port}
    explanation_mk: Уредот добива струја, но системот не го препознава. Портата не ја носи податочната врска.
    recommendations_mk:
      - Пробај директно на порта од задниот панел.
      - Избегни незасилен USB разгранувач за проверка.
  - id: rule_keyboard
    when_present: [keyboard_repeat]
    when_absent: [works_on_other_port]
    conclude: {kind: fault, id: faulty_keyboard}
    explanation_mk: Тастатурата повторува или молчи и проблемот не исчезнува на друга порта.
    recommendations_mk:
      - Пробај друга тастатура на истата порта.
      - Ако другата работи, замени ја тастатурата.
```

Ова се 8 потсистеми, 34 симптоми, 2 факти, 16 дефекти и 25 правила. Две правила заклучуваат факт што подоцна го користи правило за дефект: `power_path_dead` и `memory_subsystem_suspect`. Тоа е синџирот што машината во следната фаза мора да го помине. Не додавај трет факт.

## Начин на работа

- Вчитај ја базата преку постоечкиот репозиториум и испечати ги броевите на симптоми, дефекти, факти и правила.
- Провери ги броевите: 34, 16, 2, 25.
- Не пишувај pytest фајлови. Не повикувај `infer`.
- Ако некој македонски текст во каталогот има печатна грешка што ја менува смислата, поправи ја смислата без да го менуваш идентификаторот.

## Критериуми за прифаќање

- `load()` завршува без `KnowledgeBaseError`.
- Идентификаторите се точно оние од каталогот.
- Секој симптом има потсистем, назив и опис на македонски.
- Секое правило за дефект има објаснување и барем една препорака. Правилата за факти имаат празни препораки.
- UI и `infer` не се сменети.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не кодирај правила во Python. Не додавај сигурносни фактори, тежини, веројатности, ниту втор фајл со знаење. Не ги менувај `prompts/` и `.cursor/rules`.
