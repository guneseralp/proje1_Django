VISION_DETAIL = '''
<div class="row">
            <div class="col-sm-8 offset-sm-2">
                <h2>Vizyonumuz</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor, quo.</p>
                <p>Sequi in fugiat voluptas! Dignissimos temporibus nihil accusamus placeat blanditiis!</p>
                <p>Unde eum nam eligendi, amet nisi doloribus ex debitis a!</p>
                
                
            </div>
        </div>
'''

ABOUT_US_DETAIL = '''
<div class="row">
            <div class="col-sm-8 offset-sm-2">
                <h2>Vizyonumuz</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor, quo.</p>
                <p>Sequi in fugiat voluptas! Dignissimos temporibus nihil accusamus placeat blanditiis!</p>
                <p>Unde eum nam eligendi, amet nisi doloribus ex debitis a!</p>
                <hr>
                <h2>Misyonumuz</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor, quo.</p>
                <p>Sequi in fugiat voluptas! Dignissimos temporibus nihil accusamus placeat blanditiis!</p>
                <p>Unde eum nam eligendi, amet nisi doloribus ex debitis a!</p>
            </div>
        </div>
'''

CONTACT_DETAIL ='''
<div class="row">
            <div class="col-sm-8 offset-sm-2">
                <h2>Adresimiz</h2>
                <address>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores vel quis iusto animi impedit, voluptatibus voluptas ipsam omnis exercitationem eius.</p>
                </address>
                <hr>
                <h2>Bize Ulasin</h2>
                <form class="row g-3">
                    <div class="col-12">
                      <label for="inputEmail4" class="form-label">Email</label>
                      <input type="email" class="form-control" id="inputEmail4">
                    </div>
                    
                    
                        <div class="col-12">
                            <label for="bilgi" class="form-label">Comments</label>
                            <textarea class="form-control" id="bilgi"></textarea>
                            
                        </div>
                    
                    
                    <div class="col-md-12">
                      <label for="inputCity" class="form-label">Şehir</label>
                      <input type="text" class="form-control" id="inputCity">
                    </div>
                    <div class="col-12">
                      <label for="inputState" class="form-label">Bize Nasıl Ulaştın</label>
                      <select id="inputState" class="form-select">
                        <option selected>Seçiminiz...</option>
                        <option>Sosyal Medya</option>
                        <option>Google</option>
                        <option>Reklam</option>
                        <option>Referans</option>
                      </select>
                    </div>
                    
                    
                    <div class="col-12">
                      <button type="submit" class="btn btn-primary">Sign in</button>
                    </div>
                  </form>
            </div>
        </div>

'''

FAKE_DB_PAGES =[
    {"url": "iletisim", "detail": CONTACT_DETAIL,"title": "İletişim"},
    {"url": "hakkimizda","detail": ABOUT_US_DETAIL,"title": "Hakkımızda"},
    {"url": "vizyonumuz","detail": VISION_DETAIL,"title": "Vizyonumuz"},
]   