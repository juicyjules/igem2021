import sys
template='''
<div class="member py-5 container-md">
    <div class="member-name w-100 pb-3 " id="head-%num">%name</div>
    <div class="d-flex flex-wrap flex-md-nowrap justify-content">
        <div class="member-image">
            <img src="https://via.placeholder.com/250">
        </div>
        <div class="member-info">
            <div class="row">
                <div class="col-6">Age</div>
                <div class="col-6">%age</div>
            </div>
            <div class="row">
                <div class="col-6">Field of Study</div>
                <div class="col-6">%field</div>
            </div>
            <div class="row">
                <div class="col-6">Semester</div>
                <div class="col-6">%semester</div>
            </div>
            <div class="row">
                <div class="col-6">Favorite organism</div>
                <div class="col-6">%organism</div>
            </div>
            <div class="row">
                <div class="col-6">Fun Fact</div>
                <div class="col-6">%fact</div>
            </div>
        </div>
    </div>
</div>
'''
placeholders=["name","age","field","semester","organism","fact"]
def fill(person,num):
    res = template
    res=res.replace("%num",str(num))
    for placeholder in placeholders:
        res = res.replace(f"%{placeholder}",person[placeholder])
    return res
def parse(path):
    with open(path) as file:
        persons = []
        while line := file.readline():
            person = {}
            if line.startswith("\n"):
                continue
            for p in placeholders:
                person[p] = line.strip()
                line = file.readline()
            persons.append(person)  
    return persons
if __name__ == "__main__":
    if len(sys.argv) > 1:
        contents = parse(sys.argv[1])
        final=""
        for num,content in enumerate(contents):
            final+=fill(content,num)+"\n"
        print(final)